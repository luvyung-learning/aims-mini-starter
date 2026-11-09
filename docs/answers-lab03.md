# Lab 03 – Discussion Answers

## 1. What is a merge base?

Merge base là commit tổ tiên chung gần nhất của hai nhánh đang được tích hợp. Git sử dụng nó làm cơ sở để so sánh những thay đổi trên hai nhánh và xác định cách kết hợp nội dung.

## 2. Why should master and release/* use revert instead of reset?

Master và release/* là các nhánh đã được chia sẻ. Reset có thể viết lại lịch sử và gây mất đồng bộ giữa các bản repository. Revert tạo commit đảo ngược mới mà không xóa lịch sử đã chia sẻ.

## 3. Why should a regression test fail before the bug is fixed?

Test phải thất bại trước khi sửa để chứng minh nó có khả năng tái hiện lỗi. Sau khi sửa, test chuyển sang PASS, trở thành regression test nhằm phát hiện lỗi tương tự nếu chúng xuất hiện trở lại.

## 4. Why should a bugfix branch be created from the feature branch when the bug belongs to an unfinished feature?

Nhánh feature chứa mã nguồn của chức năng đang phát triển. Tạo bugfix từ feature giúp tái hiện lỗi trong đúng ngữ cảnh và đưa bản sửa về đúng nhánh chứa chức năng đó.

## 5. Why does a merge commit require the -m option when reverting?

Merge commit có nhiều parent. Tham số -m 1 chỉ định parent thứ nhất làm mainline để Git xác định phần thay đổi cần đảo ngược.

## 6. How do reset and revert differ?

Reset di chuyển con trỏ nhánh và có thể viết lại lịch sử. Revert tạo commit mới để đảo ngược nội dung của commit trước đó. Reset phù hợp với commit chưa chia sẻ, còn revert phù hợp với lịch sử chung.