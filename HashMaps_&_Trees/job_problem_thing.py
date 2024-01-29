# Python program for weighted job scheduling using Naive Recursive Method

def naive_recursive():
    # A job has start time, finish time, and profit.
    class Job:
        def __init__(self, start, finish, profit):
            self.start = start
            self.finish = finish
            self.profit = profit

    def job_comparator(s1, s2):
        return s1.finish < s2.finish

    # Find the latest job (in a sorted array) that doesn't
    # conflict with the job[i]. If there is no compatible job,
    # then it returns -1.
    def latest_non_conflict(arr, i):
        for j in range(i - 1, -1, -1):
            if arr[j].finish <= arr[i - 1].start:
                return j
        return -1

    # A recursive function that returns the maximum possible
    # profit from the given array of jobs. The array of jobs must
    # be sorted according to finish time.
    def find_max_profit_rec(arr, length):
        # Base case
        if length == 1:
            return arr[length - 1].profit
        # Find profit when the current job is included
        incl_prof = arr[length - 1].profit
        i = latest_non_conflict(arr, length)
        if i != -1:
            incl_prof += find_max_profit_rec(arr, i + 1)

        # Find profit when the current job is excluded
        excl_prof = find_max_profit_rec(arr, length - 1)

        return max(incl_prof, excl_prof)

    # The main function that returns the maximum possible
    # profit from the given array of jobs
    def find_max_profit(arr, n):
        # Sort jobs according to finish time
        arr.sort(key=lambda x: x.finish)

        return find_max_profit_rec(arr, n)

    if __name__ == "__main__":
        arr = [Job(3, 10, 20), Job(1, 11, 50), Job(6, 19, 100), Job(10, 12, 200)]
        print("The optimal profit is", find_max_profit(arr, len(arr)))



# Implementing using Dynamic Programming

# Python program for weighted job scheduling using Dynamic

# A job has start time, finish time, and profit.

def dynamic_programming():
    class Job:
        def __init__(self, start, finish, profit):
            self.start = start
            self.finish = finish
            self.profit = profit

    def job_comparator(s1, s2):
        return s1.finish < s2.finish

    # Find the latest job (in sorted array) that doesn't
    # conflict with the job[i]
    def latest_non_conflict(arr, i):
        for j in range(i - 1, -1, -1):
            if arr[j].finish <= arr[i - 1].start:
                return j
        return -1

    # The main function that returns the maximum possible
    # profit from given array of jobs

    def find_max_profit(arr, n):
        # Sort jobs according to finish time
        arr.sort(key=lambda x: x.finish)

        # Create an array to store solutions of subproblems. table[i]
        # stores the profit for jobs till arr[i] (including arr[i])
        table = [0 for _ in range(n)]

        table[0] = arr[0].profit

        # Fill entries in table[] using recursive property
        for i in range(1, n):

            # Find profit including the current job
            incl_prof = arr[i].profit
            l = latest_non_conflict(arr, i)
            if l != -1:
                incl_prof += table[l]

            # Store maximum of including and excluding
            table[i] = max(incl_prof, table[i - 1])

        return table[n - 1]

    if __name__ == "__main__":
        arr = [Job(3, 10, 20), Job(1, 11, 50), Job(6, 19, 100), Job(10, 12, 200)]
        print("The optimal profit is", find_max_profit(arr, len(arr)))


# naive_recursive()
# dynamic_programming()






















    # Python3 code for the above approach

    # function to schedule the jobs take 2
    # arguments array and no of jobs to schedule

def greedy_solution():
    def printJobScheduling(arr, t):

        # length of array
        n = len(arr)

        # Sort all jobs according to
        # decreasing order of profit
        for i in range(n):
            for j in range(n - 1 - i):
                if arr[j][2] < arr[j + 1][2]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # To keep track of free time slots
        result = [False] * t

        # To store result (Sequence of jobs)
        job = ['-1'] * t

        # Iterate through all given jobs
        for i in range(len(arr)):

            # Find a free slot for this job
            # (Note that we start from the
            # last possible slot)
            for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

                # Free slot found
                if result[j] is False:
                    result[j] = True
                    job[j] = arr[i][0]
                    break
        print(job)

    if __name__ == '__main__':
        arr = [['a', 2, 100], # Job Array
                ['b', 1, 19],
                ['c', 2, 27],
                ['d', 1, 25],
                ['e', 3, 15]]


        print("Following is maximum profit sequence of jobs")

        # Function Call
        printJobScheduling(arr, 3)

greedy_solution()