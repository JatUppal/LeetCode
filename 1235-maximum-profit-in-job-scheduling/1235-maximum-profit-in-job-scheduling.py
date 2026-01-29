from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Zip the job info together so each job is (end, start, profit)
        # We sort by end time to make "best profit up to this end time" easy to build.
        jobs = sorted(zip(endTime, startTime, profit))
        # Separate list of end times only, so we can binary search quickly
        ends = [e for e, s, p in jobs]
        # dp[i] = max profit we can earn using jobs[0..i] (first i+1 jobs in this sorted list)
        dp = [0] * len(jobs)
        # Process jobs in increasing end time order
        for i, (e, s, p) in enumerate(jobs):
            # Option A: TAKE this job
            take = p  # we always get this job's profit if we take it
            # Find the last job that finishes on/before this job starts (non-overlap allowed at equality)
            # bisect_right gives the insertion point for s, so subtract 1 to get the index of last <= s
            j = bisect.bisect_right(ends, s) - 1
            # If there is a compatible previous job, add its best profit
            if j >= 0:
                take += dp[j]
            # Option B: SKIP this job (best profit we already had up to previous job)
            skip = dp[i - 1] if i > 0 else 0
            # Best up to i = max of taking vs skipping
            dp[i] = max(skip, take)
        # Final answer: best profit after considering all jobs
        return dp[-1] if dp else 0
