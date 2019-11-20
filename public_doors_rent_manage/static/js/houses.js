/**
 * 提交房产表单查询
 */
function searchHouse() {
    document.searchHouseForm.submit();
    
}
/**
 * 新作房产数据
 */
function gotoHouseInput() {
    window.location.href = 'house_detail?mode=添加';
}
/**
 * 删除房产数据
 */
function deleteHouse(housecode) {
    var msg = '确定要删除：' + housecode + ' 吗？';
    if (!confirm(msg)) {
        return;
    }
    window.location.href = 'houses?mode=del&house_code=' + housecode
}
/**
 * 跳转到房产列表信息页
 */
function backToHouses() {
    //alert("hello");
    window.location.href='houses?mode=all';
}