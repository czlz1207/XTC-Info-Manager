# XTC-Info-Manager

Manage Xtcinfo Partition For XTC-Device By Python.

Original Project By Kotlin: [huanli233/XTCInfoManager](https://github.com/huanli233/XTCInfoManager)

---

**Feature**

1. Read XTC-Device's SelfRsaKey And Keyid From Your XtcInfo Partition File.

```
$ xtcInfoMgr read <path/to/your/img/file>
```

2. Write New SelfRsaKey(Required) And Keyid(Optional) To Your XtcInfo File.

```
$ xtcInfoMgr write <path/to/yout/img/file> <selfRsaKey> <keyid(Optional)>
```
