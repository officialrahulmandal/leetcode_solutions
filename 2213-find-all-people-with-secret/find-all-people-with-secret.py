class Solution:
    def findAllPeople(self, n, meetings, firstPerson) :
        # person 0, and firstPerson already knows the secret
        knowsSecret = set([0, firstPerson])
        
        # after sort the meeting by time, the same time meeting will be grouped together
        # so we can relie on people that knows secret before that time from "knowsSecret"
        sortedMeetings = []
        meetings.sort(key=lambda x:x[2]) # O(M*log(M))
        
        # tracking every meeting times to decide if current meeting has same time as previous meeting
        seenTime = set()
        
        # building the sortedMeetings as explained above
        for meeting in meetings: # O(M)
            if meeting[2] not in seenTime:
                seenTime.add(meeting[2])
                sortedMeetings.append([])
            sortedMeetings[-1].append((meeting[0], meeting[1]))

        # we then now will build graph for each meeting time, and traverse(BFS) the graph from
        # people that already knows the secret to find more people who knows secret
        for meetingGroup in sortedMeetings: #O(T)
            # q needs to be set then push to queue, because of duplicate values we find from meetings
            # otherwise it will reach the TLE
            pplKnowSecret = set()
            graph = defaultdict(list)
            
            # building bidirectional graph, and make sure to build our queue as well if we find
            # a person who knows secret
            for p1, p2 in meetingGroup: # ~O(M/T)
                graph[p1].append(p2)
                graph[p2].append(p1)
                if p1 in knowsSecret:
                    pplKnowSecret.add(p1)
                if p2 in knowsSecret:
                    pplKnowSecret.add(p2)
                    
            # adding people that already knows the secret to start off our graph traversal 
            queue = deque((pplKnowSecret)) # O(n)
        
            while queue: # ~O(M/T)
                curr = queue.popleft()
                #any1 we find from our queue knows secret, so record it
                knowsSecret.add(curr)
                for neigh in graph[curr]:
                    if neigh not in knowsSecret:
                        knowsSecret.add(neigh)
                        queue.append(neigh)

        return list(knowsSecret)