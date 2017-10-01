def whoami():
    def local_groot():
        i = "I am local groot"
        print(i)

    def nonlocal_groot():
        nonlocal i
        i = "I am nonlocal groot"

    def global_groot(name):
        return "I am {0} groot".format(name)

    i = "I am groot"
    print(i)
    local_groot()
    print(i)
    nonlocal_groot()
    print(i)
    print(global_groot("the only"))
    print(i)

whoami()