import csv

def save_to_file(jobs, word):
  file = open(f'csv/{word}.csv', mode='w', encoding='utf-8')
  writer = csv.writer(file)
  writer.writerow(['Title', 'Company', 'Location', 'Link'])
  for job in jobs:
    writer.writerow(list(job.values()))
  return