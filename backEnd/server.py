import websockets
import asyncio
import os
from convert_to_json import ConvertToJSON
from file_watcher import FileWatcher

PORT = 1337

print("Server is listening on port: ", PORT)


async def Watcher(websocket, path):
    fileName = "sample.log"
    # watch = FileWatcher(fileName)
    # while True:
    #     if watch.HasChanged():
    linesToBeRead = 10
    bufSize = 8192
    fileSize = os.stat(fileName).st_size
    counter = 0
    with open(fileName) as f:
        while True:
            if bufSize > fileSize:
                bufSize = fileSize-1
                fetchedLines = []

                while True:
                    counter += 1
                    position = (fileSize-bufSize)*counter

                    f.seek(position)

                    fetchedLines.extend(f.readlines())
                    if len(fetchedLines) >= linesToBeRead or f.tell() == 0:
                        lastTenLines = fetchedLines[-linesToBeRead:]
                        JSON = ConvertToJSON(lastTenLines)
                        await websocket.send(JSON)
                        break

            lastUpdate = f.readline()
            while not lastUpdate:
                await asyncio.sleep(5)
                lastUpdate = f.readline()
            JSON = ConvertToJSON(lastUpdate)
            await websocket.send(JSON)


server = websockets.serve(Watcher, "localhost", PORT)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
