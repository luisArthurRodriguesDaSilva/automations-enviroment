import os
from . import runModel
from . import mainModel

run_model = runModel.run_model
main_model = mainModel.main_model


def main():
    current_path = os.getcwd()
    dir_paths = list(map(lambda x: os.path.join(current_path, x), ["src", "resources"]))

    for path in dir_paths:
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
            print(f"{path} is created")

    for model in [(main_model, "main.py"), (run_model, "run.py")]:
        with open(os.path.join(dir_paths[0], model[1]), "w") as run:
            run.write(model[0])
