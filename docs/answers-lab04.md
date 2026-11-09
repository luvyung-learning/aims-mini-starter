# Lab 04 – Discussion Answers

## 1. Why should release branches never be merged back into master?

Release branch đại diện cho một dòng bảo trì của phiên bản đã phát hành, còn master tiếp tục phát triển phiên bản mới. Merge ngược có thể đưa các thay đổi đặc thù của phiên bản cũ vào phiên bản mới và gây xung đột về mã nguồn hoặc version. Khi cần chuyển bản sửa lỗi, nên sử dụng cherry-pick.

## 2. How does Release Flow differ from GitFlow?

Release Flow trong học phần sử dụng master làm nhánh phát triển chính và release/* làm dòng bảo trì phiên bản đã nộp. GitFlow sử dụng main, develop cùng các nhánh feature, release và hotfix theo quy trình riêng. Release Flow của học phần được đơn giản hóa để phù hợp với bài thực hành và quản lý các bản nộp theo tuần.

## 3. Why does the project move from 0.3.0 to 1.0.0 instead of 0.4.0?

Semantic Versioning sử dụng MAJOR để biểu thị một phiên bản chính thức có mức độ ổn định và cam kết tương thích. Trong học phần, v0.1.0 đến v0.3.0 được sử dụng ở giai đoạn thực hành ban đầu, còn v1.0.0 đánh dấu phiên bản phát hành chính thức đầu tiên của AIMS-mini.

## 4. Why should CHANGELOG be updated before a release?

CHANGELOG ghi lại những thay đổi đáng chú ý của phiên bản. Cập nhật trước khi phát hành giúp thông tin tài liệu khớp với mã nguồn và cung cấp cơ sở cho release notes.

## 5. Why are annotated tags important for configuration auditing?

Annotated tag lưu thông tin định danh và thông điệp mô tả phiên bản. Nó giúp xác định chính xác commit đại diện cho Baseline và hỗ trợ tái tạo, kiểm toán phiên bản đã phát hành.

## 6. How does git describe support Status Accounting?

git describe cho biết commit hiện tại gần tag nào và có bao nhiêu commit mới kể từ tag đó. Nhờ vậy, nhóm có thể xác định trạng thái phát triển tương đối so với phiên bản phát hành gần nhất.

## 7. Why is Git Worktree useful for Configuration Audit?

Git Worktree tạo thư mục làm việc độc lập cho một trạng thái hoặc nhánh khác của cùng repository. Nhờ đó, nhóm có thể chạy chương trình và kiểm thử phiên bản cũ mà không cần thay đổi nhánh phát triển hiện tại.