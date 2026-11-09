# Lab 02 – Discussion Answers

## 1. Why must master be synchronized before creating a Pull Request?

Master có thể đã nhận những thay đổi mới từ các nhánh khác. Việc đồng bộ giúp phát hiện sớm xung đột, kiểm tra khả năng tích hợp và giảm rủi ro khi merge.

## 2. When should developers avoid rebasing?

Không nên rebase các commit đã được chia sẻ và những nhánh mà thành viên khác đang sử dụng, vì rebase tạo SHA mới và viết lại lịch sử commit. Điều này có thể khiến các bản repository không đồng nhất.

## 3. How are feature/* and topic/* different?

`feature/*` tập trung phát triển một chức năng của phần mềm, chẳng hạn tìm kiếm DVD hoặc in giỏ hàng. `topic/*` tập trung vào một chủ đề hoặc công việc cụ thể như tạo Pull Request template, sơ đồ Use Case hoặc cấu hình CI.

Cả hai đều được tạo từ master và tích hợp thông qua Pull Request.

## 4. Why should stale approvals be dismissed after new commits?

Khi tác giả push thêm commit sau khi được approve, nội dung PR đã thay đổi. Việc yêu cầu review lại bảo đảm phiên bản được tích hợp chính là phiên bản đã được phê duyệt.

## 5. Compare Merge Commit, Squash and Rebase.

Merge Commit giữ lịch sử commit của nhánh và tạo một merge commit. Squash gộp nhiều commit thành một commit tổng hợp. Rebase áp dụng lại các commit trên nền mới, tạo SHA mới và giữ lịch sử tuyến tính.

Merge Commit phù hợp khi cần lưu lịch sử chi tiết; Squash phù hợp khi muốn lịch sử gọn; Rebase phù hợp khi muốn lịch sử tuyến tính.