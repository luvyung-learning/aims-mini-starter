# Lab 01 – Discussion Answers

## 1. Why is git mv used instead of manually deleting and recreating files?

git mv giúp di chuyển hoặc đổi tên tệp trong repository và đưa thay đổi vào Git Index. Git có thể nhận diện sự tương đồng giữa tệp cũ và tệp mới, nhờ đó hỗ trợ theo dõi lịch sử qua quá trình refactoring.

## 2. Is release/lab01 a baseline? Why?

Có. release/lab01 lưu trạng thái mã nguồn đã hoàn thành và được lựa chọn làm phiên bản nộp bài. Nhánh này đại diện cho một cấu hình đã thống nhất, có thể được kiểm tra và tái tạo.

## 3. Why should developers not commit directly to master even when working alone?

Không commit trực tiếp lên master giúp duy trì quy trình kiểm soát thay đổi nhất quán. Pull Request tạo điểm kiểm tra để xem xét nội dung, kiểm thử và lịch sử trước khi tích hợp, kể cả khi chỉ có một người phát triển.