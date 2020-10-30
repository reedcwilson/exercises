'''
A company needs to create a mechanism to group emails into threads.  They know
that grouping by the subject line is unreliable. They want to compare body text
instead.  Each message starts with the reply text, followed by "---" and then
the quoted email from the thread.  The sender and receiver in a thread must
also match, though their roles may reverse.

Implement a solution to group emails into threads. It should return a
2-dimensional array with the thread number of each email and its position in
the thread, as integers. Messages are indexed starting at 1.

Example:
n = 3
emails = [
    ('alex@gmail.com', 'sam@gmail.com', 'Are you back?'),
    ('chris@gmail.com', 'robin@gmail.com', 'did you get the key?'),
    ('sam@gmail.com', 'alex@gmail.com', 'Just got in.---Are you back?')
].

There are two threads in the emails. In this case, the output should be [(1,
1), (2, 1), (1, 2)]. This signifies that the first email is in thread 1 and its
position is 1, the second email is in thread 2 and its position in that thread
is 1, and the third email is in the thread 1, position 2.

Function Description
Complete the function getEmailThreads in the editor below. The function must
return a 2D array.


getEmailThreads has the following parameter(s):
    emails[emails[0],...emails[n-1]]:  an array of strings

Constraints
===========
1 ≤ n ≤ 700
- The maximum length of a mail won't exceed 200
- The email body will contain only lowercase English letters, blank space,
  comma, period and question mark.
_ The email of a person will contain only lowercase English letters, at the
  rate (@) sign, and period.
'''


class Email:
    def __init__(self, from_person, to_person, message):
        self._participants = [from_person.strip(), to_person.strip()]
        self._parts = message.strip().split('---')
        self._root = self._parts[-1]

    @property
    def key(self):
        p = '|'.join(sorted(self._participants))
        return '{}|{}'.format(p, self._root)

    @property
    def position(self):
        return len(self._parts)


def getEmailThreads(emails):
    threads = []
    result = []
    for e in emails:
        parts = e.split(',')
        email = Email(parts[0], parts[1], ','.join(parts[2:]))
        try:
            idx = threads.index(email.key)
            result.append([idx + 1, email.position])
        except ValueError:
            threads.append(email.key)
            result.append([len(threads), email.position])
    return result


if __name__ == '__main__':
    emails = [
        'abc@gmail.com, x@gmail.com, hello x, how are you?',
        'c@gmail.com, abc@gmail.com, did you take a look at the event?',
        'x@gmail.com, abc@gmail.com, i am great. how are you?---hello x, how are you?',  # NOQA
    ]
    result = getEmailThreads(emails)
    print(result)
