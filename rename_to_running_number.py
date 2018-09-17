import sys, glob, os

running_no = 1;
working_dir = sys.argv[1]
for old_name in glob.iglob("%s\*" % working_dir):
    title, ext = os.path.splitext(os.path.basename(old_name))
    new_name = "%s\%04d%s" % ( working_dir, running_no, ext )

    os.rename(old_name, new_name)
    #print("%s -> %s" % (old_name, new_name))

    running_no += 1
