from ast import literal_eval

# the prescribed data structure in the Raft paper to 
# add entries
class AppendEntriesCall:
    def __init__(self, in_term, previous_index, previous_term, entries):
        self.in_term = in_term
        self.previous_index = previous_index
        self.previous_term = previous_term
        self.entries = entries

    def to_message(self):
        return "append_entries in_term " \
                + str(self.in_term) + \
                " after " +\
                str(self.previous_index) + " " + \
               str(self.previous_term) + " @" + \
               str(self.entries)

    @classmethod
    def from_message(cls, message):
        context, entries_as_string = message.split("@")
        numeric_markers = context.replace("append_entries in_term ", "").split(" ")
        current_term, index, latest_log_term = int(numeric_markers[0]), int(numeric_markers[2]), int(numeric_markers[3])
        entries = literal_eval(entries_as_string)

        return AppendEntriesCall(
            in_term=current_term,
            previous_index=index,
            previous_term= latest_log_term,
            entries=entries
        )


class RequestVoteCall:
    def __init__(self, for_term, latest_log_index, latest_log_term):
        self.for_term = for_term
        self.latest_log_index = latest_log_index
        self.latest_log_term = latest_log_term

    def to_message(self):
        return "can_I_count_on_your_vote_in_term " \
                + str(self.for_term) \
                + " ? " \
                + "last_log_entry: " \
                + str(self.latest_log_index) \
                + " " \
                + str(self.latest_log_term)

    @classmethod
    def from_message(cls, message):
        numeric_markers = message.replace("can_I_count_on_your_vote_in_term ", "").split(" ")
        current_term, index, latest_log_term = int(numeric_markers[0]), int(numeric_markers[3]), int(numeric_markers[4])

        return RequestVoteCall(
            for_term=current_term,
            latest_log_index=index,
            latest_log_term=latest_log_term,
        )

class LogDataAccessObject:

    def __init__(self, array, dict):
        self.ordered_logs = array
        self.term_indexed_logs = dict
    

