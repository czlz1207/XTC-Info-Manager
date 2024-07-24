def read_key(path: str):
    with open(path, 'r', errors='ignore') as file:
        content = file.read()
    key_start_position = 2057
    key_length = 159
    extracted = content[key_start_position:key_start_position + key_length]

    key_parts = extracted.split(":")
    key_id = key_parts[0].strip()
    key_data = key_parts[1].strip()
    return key_id, key_data


def write_key(path: str, rsa_key: str, keyid: str | None):
    import shutil
    if len(rsa_key) != 128:
        raise ValueError("Key length must be 128 characters")
    if keyid and len(keyid) != 30:
        raise ValueError("Key ID length must be 30 characters")
    backup_path = path + '.backup.img'
    shutil.copy2(path, backup_path)
    with open(backup_path, 'r', errors='ignore') as file:
        content = file.read()
    segment = content[2057:2057 + 159]

    if keyid:
        old_keyid_key = f"{segment.split(':')[0]}:{segment.split(':')[1][:128]}"
        new_keyid_key = f"{keyid}:{rsa_key}"
    else:
        old_keyid_key = f"{segment.split(':')[1][:128]}"
        new_keyid_key = rsa_key

    new_content = content.replace(old_keyid_key, new_keyid_key)

    # 写回备份文件
    with open(backup_path, 'w', errors='ignore') as file:
        file.write(new_content)


if __name__ == "__main__":
    print("---Xtc_Info_Manager v1.0")
    print("---https://github.com/czlz1207/XTC-Info-Manager/")
    import argparse

    parser = argparse.ArgumentParser(description="Read and write xtcInfo.img with RSA key information.")
    subparsers = parser.add_subparsers(dest="mode", help="Mode of operation: read or write")

    read_parser = subparsers.add_parser('read', help="file_path")
    read_parser.add_argument('file_path', type=str, help="Path of the file to read")

    write_parser = subparsers.add_parser('write', help="file_path rsa_keyid rsa_key")
    write_parser.add_argument('file_path', type=str, help="Path of the file to write")
    write_parser.add_argument('--keyid', type=str, help="RSA Key ID(Optional)")
    write_parser.add_argument('rsa_key', type=str, help="RSA Key")

    args = parser.parse_args()

    if args.mode == 'read':
        key = read_key(args.file_path)
        print(f"Your key id is {key[0]}\nYour RSA key is {key[1]}")
    elif args.mode == 'write':
        if args.keyid:
            write_key(args.file_path, args.rsa_key, args.keyid)
        else:
            write_key(args.file_path, args.rsa_key, None)
    else:
        parser.print_help()
