def fifo_page_replacement(page_requests, frame_size):
    frames = []
    page_faults = 0
    hits = 0

    for page in page_requests:
        if page in frames:
            hits += 1
            status = "Hit"
        else:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
            status = "Miss"

        print(f"Page: {page} -> Frames: {frames}, {status}")

    return page_faults, hits

page_requests = [3, 8, 2, 3, 9, 1, 6, 3, 8, 9, 3, 6, 2, 1, 3]
frame_size = 5

total_page_faults, total_hits = fifo_page_replacement(page_requests, frame_size)
print(f"Total Page Faults: {total_page_faults}")
print(f"Total Hits: {total_hits}")
