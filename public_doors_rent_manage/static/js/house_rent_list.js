/**
 * 跳转到房产列表信息页
 */
function backToHouseRentList() {
    //alert("hello");
    window.location.href='house_rent_list?mode=all';
}
/**
 * 新作房产租赁数据
 */
function gotoHouseRentInput() {
    window.location.href = 'house_rent?mode=添加';
}
/**
 * 提交房产租赁表单查询
 */
function searchHouseRent() {
    document.searchHouseRentForm.submit();
    
}
/**
 * 删除房产数据
 */
function deleteHouseRent(id, housecode) {
    var msg = '确定要删除：' + housecode + ' 的租赁信息吗？';
    if (!confirm(msg)) {
        return;
    }
    window.location.href = 'house_rent_list?mode=del&id=' + id
}