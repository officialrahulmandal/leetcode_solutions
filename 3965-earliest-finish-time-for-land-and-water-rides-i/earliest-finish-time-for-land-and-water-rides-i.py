class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def bestRideTime(firstStartTime, firstDuration, secondStartTime, secondDuration):
            firsttrip=float('inf')
            for s,d in zip(firstStartTime, firstDuration):
                firsttrip = min(firsttrip,s+d)

            secondtrip = float('inf')

            for s,d in zip(secondStartTime, secondDuration):
                secondtrip = min(secondtrip,(max(firsttrip, s)+d))

            return secondtrip

        return min(bestRideTime(landStartTime, landDuration, waterStartTime, waterDuration),bestRideTime(waterStartTime, waterDuration, landStartTime, landDuration))
