def load_work_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    work_data = {}
    for line in data:
        day, hours = line.strip().split(', ')
        work_data[int(day)] = float(hours)
    return work_data

def validate_total_hours(work_data, working_days=22):
    total_hours = sum(work_data.values())
    allowed_hours = 8 * working_days
    return total_hours <= allowed_hours, total_hours

def validate_sunday_work(work_data):
    sundays = [7, 14, 21, 28]
    for sunday in sundays:
        if work_data.get(sunday, 0) > 0:
            return False
    return True

def calculate_overtime(work_data):
    overtime = 0
    for day, hours in work_data.items():
        if day % 7 == 0: 
            overtime += hours
        elif hours > 8:
            overtime += (hours - 8)
    return overtime

def validate_break_between_days(work_data):
    for day in sorted(work_data.keys()):
        next_day_hours = work_data.get(day + 1, None)
        if next_day_hours is not None:
            time_worked_today = work_data[day]
            time_before_next_day = 24 - time_worked_today
            if time_before_next_day < 11:
                return False
    return True

if __name__ == "__main__":
    file_path = "work_hours.txt"
    work_data = load_work_data(file_path)

    print("Total Hours Validation:", validate_total_hours(work_data))
    print("Sunday Work Validation:", validate_sunday_work(work_data))
    print("Total Overtime:", calculate_overtime(work_data))
    print("Break Between Days Validation:", validate_break_between_days(work_data))