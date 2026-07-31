import os
import platform
import subprocess


def open_document(file_path):
    """
    Opens a document using the system's default PDF viewer.
    """

    # Absolute path of project root
    project_root = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )

    absolute_path = os.path.join(project_root, file_path)
    absolute_path = os.path.normpath(absolute_path)

    print("Opening:", absolute_path)

    if not os.path.exists(absolute_path):
        print("File not found.")
        return False

    try:

        if platform.system() == "Windows":
            os.startfile(absolute_path)

        elif platform.system() == "Darwin":
            subprocess.call(["open", absolute_path])

        else:
            subprocess.call(["xdg-open", absolute_path])

        return True

    except Exception as error:

        print(error)
        return False