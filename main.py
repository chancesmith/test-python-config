import json
import os
import sys

# current dir
currentDir = str(sys.argv[1])
print(f'Looking in directory: {currentDir}')

## find config file
def getConfigJson(directory):
  configPath = directory + '/config.json'
  isConfigFound = os.path.isfile(configPath)
  print(configPath, isConfigFound)

  result = json.loads('{"type": "application", "pythonVersion": 3}')

  if (isConfigFound):
    print('isConfigFound found 👍')
    jsonFile = open(configPath, "r")
    data = jsonFile.read()
    jsonFile.close()
    result = json.loads(data)

  if ('type' not in result):
    result['type'] = 'application'

  if ('pythonVersion' not in result):
    result['pythonVersion'] = 3

  if ('ignorePython' not in result):
    print("ignorePython not found")
    result['ignorePython'] = False

  return result

## loop through generated-services/
for root, dirs, files in os.walk(currentDir):
  for idx, file in enumerate(files):
    config_dict = getConfigJson(root)
    print(file, root, config_dict, config_dict['ignorePython'], config_dict['ignorePython'] == True)