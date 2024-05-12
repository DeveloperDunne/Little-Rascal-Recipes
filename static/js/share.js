const editButtons = document.getElementsByClassName("btn-edit");
const shareTitle = document.getElementById("id_title");
const shareAuthor = document.getElementById("id_author");
const sharePicture = document.getElementById("id_picture");
const shareForm = document.getElementById("shareForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let shareId = e.target.getAttribute("data-share_id");
    let shareContent = document.getElementById(`share${shareId}`).innerText;
    shareTitle.value = shareContent;
    shareAuthor.value = shareContent;
    sharePicture.value = shareContent;
    submitButton.innerText = "Update";
    shareForm.setAttribute("action", `edit_share/${shareId}`);
  });
}


for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let shareId = e.target.getAttribute("data-share_id");
    deleteConfirm.href = `delete_share/${shareId}`;
    deleteModal.show();
  });
}
