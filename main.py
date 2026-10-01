import os
import json
import platform
def os_info():
    return {
        "os_type": platform.system(),
        "os_release":platform.release(),
        "os_version":platform.version(),
        "machine":platform.machine(),
        "processor":platform.processor(),
        "architecture":platform.architecture(),
        "cpu_cores":os.cpu_count(),
        "hostname":platform.node(),
        "system":platform.system(),
        "python_version": platform.python_version(),
        "implementation": platform.python_implementation(),
        "compiler": platform.python_compiler(),
        "build": platform.python_build(),
    }
def main():
    info={
    "info":os_info(),}

    filename="system_info.json"
    with open(filename,"w",encoding="utf-8") as file:
        json.dump(info, file,indent=2,ensure_ascii=False)
    print(filename)
if __name__ == "__main__":
    main()