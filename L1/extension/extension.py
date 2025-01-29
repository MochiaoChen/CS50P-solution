s,e = input("File name:").strip().lower().split(sep =".")

match e:
    case "gif":
        print("image/gif")
    case "jpg"|"jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _ :
        print("application/octet-stream")



