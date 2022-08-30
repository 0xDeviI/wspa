import os

def wspa_to_pyc(file: str):
    if (not os.path.exists(file)):
        print("File doesn't exist!")
        exit()
    else:
        wspa_file = open(file, "r").readlines()
        for i in range(len(wspa_file)):
            wspa_file[i] = wspa_file[i].replace("\n", "")
        PY_CODE = ""
        for i in range(len(wspa_file)):
            line = wspa_file[i]
            py_segment = [line[ i : i + 2 ] for i in range(0, len(line), 2)]
            for j in range(len(py_segment)):
                if (len(py_segment[j]) == 2):
                    py_segment[j] = py_segment[j][1] + py_segment[j][0]
                PY_CODE += py_segment[j]
            PY_CODE += "\n"
        return PY_CODE

def wspa_to_py(file: str):
    py_file = os.path.basename(file).replace(".wspa", "") + ".py"
    open(py_file, "w+").write(wspa_to_pyc(file))

def py_to_wspa(file: str):
    if (not os.path.exists(file)):
        print("File doesn't exist!")
        exit()
    else:
        py_file = open(file, "r").readlines()
        py_file.append("print('a code From WSPA (swap01) by Armin Asefi: https://github.com/0xDeviI/wspa')")
        for i in range(len(py_file)):
            py_file[i] = py_file[i].replace("\n", "")
        WSPA_CODE = ""
        for i in range(len(py_file)):
            line = py_file[i]
            wspa_segment = [line[ i : i + 2 ] for i in range(0, len(line), 2)]
            for j in range(len(wspa_segment)):
                if (len(wspa_segment[j]) == 2):
                    wspa_segment[j] = wspa_segment[j][1] + wspa_segment[j][0]
                WSPA_CODE += wspa_segment[j]
            WSPA_CODE += "\n"
        wspa_file = os.path.basename(file).replace(".py", "") + ".wspa"
        open(wspa_file, "w+").write(WSPA_CODE)