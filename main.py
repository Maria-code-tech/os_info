import os
import json
import platform
def os_info():
    info= {
        "os_type": platform.system(),
        "os_release":platform.release(),
        "os_version":platform.version(),
        "machine":platform.machine(),
        "processor":platform.processor(),
        "architecture":platform.architecture(),
        "cpu_cores":os.cpu_count(),
        "hostname":platform.node(),
        "python_version": platform.python_version(),
        "implementation": platform.python_implementation(),
        "compiler": platform.python_compiler(),
        "build": platform.python_build(),
    }
    current_os = platform.system().lower()

    #параметры для Windows
    if current_os == "windows":
        info["win_edition"] = platform.win32_edition()
        info["win_ver_tuple"] = platform.win32_ver()
        # Можно добавить переменные окружения Windows (например, папку AppData)
        info["appdata_path"] = os.environ.get("APPDATA")
    #параметры для Linux
    elif current_os == "linux":
        try:
            info["linux_distribution"] = platform.freedesktop_os_release().get("NAME", "Unknown Linux")
        except AttributeError:
            info["linux_distribution"] = "Linux (Unknown Distro)"
    return info

def main():
    info = {
        "info": os_info(),
    }
    filename = "system_info.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(info, file, indent=2, ensure_ascii=False)
    print(f"Файл сохранен: {filename}")

if __name__ == "__main__":
    main()