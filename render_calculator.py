fps_ = int(input("enter fps of animation: "));
tpf_ = int(input("enter time(s) to render frame: "));
length_ = float(input("enter length(s) of animation: "));

total_time = fps_ * tpf_ * length_;
#print(total_time);
hours_ = total_time // 3600;
total_time -= hours_ * 3600;
minutes_ = total_time / 60;

print(f"{hours_} hours {minutes_} minutes");