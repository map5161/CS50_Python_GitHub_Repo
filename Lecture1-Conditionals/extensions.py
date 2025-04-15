def match_name(name):
    match name:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


file_name = input("File: ").strip().lower()


if file_name.count(".") == 2:
    file_name2 = file_name.split(".", 2)[2]
    match_name(file_name2)
elif "." in file_name:
    file_name2 = file_name.split(".", 1,)[1]
    match_name(file_name2)
else:
    print("application/octet-stream")


