class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        rooms = {}
        index = 1

        for i in intervals:
            if index == 1:
                rooms[1] = i.end
                index += 1
            else:
                fit = False
                for r, e in rooms.items():
                    if i.start >= e:
                        rooms[r] = i.end
                        fit = True
                        break
                if not fit:
                    rooms[index] = i.end
                    index += 1

        return index - 1