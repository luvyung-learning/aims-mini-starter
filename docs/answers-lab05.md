# Lab 05 – Discussion Answers

## 1. What are the advantages and disadvantages of Upstream-first compared with Release-first?

Release-first tạo hotfix từ release branch, sửa phiên bản đã phát hành trước rồi lan truyền bản sửa sang master. Phương pháp này phù hợp khi cần ưu tiên bảo trì phiên bản đang được sử dụng.

Upstream-first sửa lỗi trên master trước rồi cherry-pick sang các release branch. Phương pháp này giúp dòng phát triển chính giữ vai trò nguồn thay đổi chuẩn, nhưng cần kiểm tra tính tương thích với từng phiên bản cũ.

## 2. Which command can detect a fix that has not been propagated to release/lab05?

Có thể sử dụng `git log`, `git cherry` và tìm kiếm commit có thông tin cherry-pick trong lịch sử. `git cherry` giúp xác định những thay đổi tương đương đã có hoặc chưa có giữa hai nhánh, kể cả khi SHA khác nhau.

## 3. Why should the bug-fix commit and version-bump commit be separated?

Commit sửa lỗi cần được lan truyền sang nhiều dòng phiên bản, trong khi commit nâng version chỉ áp dụng cho dòng release cụ thể. Tách hai commit giúp cherry-pick đúng phần cần thiết và tránh xung đột version giữa các nhánh.

## 4. Why is cherry-pick -x used instead of merging the entire hotfix branch?

Cherry-pick -x chỉ lấy một commit cụ thể và bổ sung thông tin nguồn gốc của commit đó. Cách này giúp đưa bản sửa lỗi sang các nhánh khác mà không đưa theo commit nâng version của dòng release ban đầu.

## 5. Why was tag v1.1.0 not created before the hotfix was integrated?

Vì release/lab05 chưa hoàn thiện khi mới được tạo. Nếu gắn tag trước khi tích hợp bản sửa, tag sẽ không đại diện cho trạng thái cuối cùng dự kiến phát hành. Khi đó cần tạo một phiên bản PATCH tiếp theo nếu muốn phát hành thay đổi mới mà vẫn giữ nguyên tag cũ.

## 6. How does Configuration Audit verify that a fix exists across multiple versions?

Configuration Audit sử dụng git log, git cherry, git tag --contains và kiểm thử hành vi trên từng phiên bản. Việc kiểm tra nhiều nguồn giúp xác nhận bản sửa đã được lan truyền đầy đủ và vẫn hoạt động đúng trên từng dòng phiên bản.

## 7. How does GitHub Actions prevent defective code from being merged?

GitHub Actions tự động chạy unit test khi có Pull Request hoặc push theo cấu hình. Khi test thất bại, status check không đạt. Nếu Branch Protection yêu cầu status check thành công, GitHub sẽ khóa thao tác merge.

## 8. How can AI improve the CI/CD workflow?

AI có thể hỗ trợ sinh mã, review Pull Request, tạo test case, phát hiện edge case, cập nhật dependency, dự đoán lỗi build và quét lỗ hổng bảo mật. Tuy nhiên, mã do AI tạo ra vẫn cần được review và kiểm thử trước khi merge.