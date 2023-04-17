#steps are things that happen during the event
#each step has a name, a description, a duration, a list of supplier GASs, a list of members enjouing the step, and a list of members organizing the step
#steps also have 2 lists of tags, one for the members enjoying the step, and one for the members organizing the step
#steps also refer to sinular member that is responsible for the step
#steps may also have a start time and end time, but these are not required
#steps also contain a list of steps that must be completed before the step can be started - this is initially empty, but is filled in by the program
#steps also contain a list of steps that happen after the step - this is initially empty, but is filled in by the program

class step:
    def __init__(self, name, description, duration, GASs, enjouers, organizers, enjouer_tags, organizer_tags, responsible, start_time=None, end_time=None, pre_steps=None, post_steps=None):
        self.name = name
        self.description = description
        self.duration = duration
        self.GASs = GASs
        self.enjouers = enjouers
        self.organizers = organizers
        self.enjouer_tags = enjouer_tags
        self.organizer_tags = organizer_tags
        self.responsible = responsible
        self.start_time = start_time
        self.end_time = end_time
        self.pre_steps = pre_steps
        self.post_steps = post_steps