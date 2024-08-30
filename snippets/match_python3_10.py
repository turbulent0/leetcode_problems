
# compare structures
l_ = [1, 2, 4]

match l_:
    case  [1, 2, 3]:
        print(True)
        # This is a "Cl_ose with comment" comment. Don't do anything for the
        # comment, because we'l_l_ al_so get a "pul_l_ request cl_osed" event at
        # the same time, and it wil_l_ do whatever we need.
        pass