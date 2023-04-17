#members are classes of persons that are involved in the event
#members can be individuals or groups
#members that are groups point to a name file that contains the names of persons in the group
#members are either enjoyers or organizers, this is called the involvement
#members can have tags that are used to involve or inform them of a step

#member is a class, and indiv and group are derived classes

class member:
    def __init__(self, name, involvement, tags):
        self.name = name
        self.involvement = involvement
        self.tags = tags

class indiv(member):
    def __init__(self, name, involvement, tags):
        member.__init__(self, name, involvement, tags)
        self.isgroup = False

class group(member):
    def __init__(self, name, involvement, tags, names):
        member.__init__(self, name, involvement, tags)
        self.isgroup = True
        self.names = names



