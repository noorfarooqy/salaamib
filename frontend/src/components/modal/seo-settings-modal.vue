<template>
  <!-- Add New Modal -->
  <div class="modal custom-modal custom-lg-modal fade" id="add_custom" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Email Template</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body add">
          <div class="addnew-modal">
            <form action="#">
              <div class="row">
                <div class="col-lg-12 col-sm-12">
                  <div class="input-block mb-3">
                    <label>Title</label>
                    <input type="text" class="form-control" placeholder="Enter Title" />
                  </div>
                </div>
                <div class="col-lg-12 col-sm-12">
                  <div class="input-block mb-3">
                    <label>Subject</label>
                    <input type="text" class="form-control" placeholder="Enter Subject" />
                  </div>
                </div>
                <div class="col-md-12 description-box">
                  <div class="input-block mb-3">
                    <label class="form-control-label">Template Content</label>
                    <editor v-model="content" />
                  </div>
                </div>
              </div>
            </form>

            <div class="modal-footer">
              <button
                type="button"
                data-bs-dismiss="modal"
                class="btn btn-back cancel-btn me-2"
              >
                Cancel
              </button>
              <button
                type="submit"
                data-bs-dismiss="modal"
                class="btn btn-primary paid-continue-btn"
              >
                Add New
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Vendor Modal -->

  <!-- Edit Modal -->
  <div class="modal custom-modal custom-lg-modal fade" id="edit_email" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Email Template</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body add">
          <div class="addnew-modal">
            <form action="#">
              <div class="row">
                <div class="col-lg-12 col-sm-12">
                  <div class="input-block mb-3">
                    <label>Title</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter Title"
                      value="Welcome Email"
                    />
                  </div>
                </div>
                <div class="col-lg-12 col-sm-12">
                  <div class="input-block mb-3">
                    <label>Subject</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter Subject"
                      value="Welcome [Username]"
                    />
                  </div>
                </div>
                <div class="col-md-12 description-box">
                  <div class="input-block mb-3">
                    <label class="form-control-label">Template Content</label>
                    <editor v-model="content1" />
                  </div>
                </div>
              </div>
            </form>

            <div class="modal-footer">
              <button
                type="button"
                data-bs-dismiss="modal"
                class="btn btn-back cancel-btn me-2"
              >
                Cancel
              </button>
              <button
                type="submit"
                data-bs-dismiss="modal"
                class="btn btn-primary paid-continue-btn"
              >
                Save Changes
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Modal -->

  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade modal-delete" id="delete_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <div class="delete-modal-icon">
              <span><i class="feather feather-check-circle"></i></span>
            </div>
            <h3>Are You Sure?</h3>
            <p>You want delete email template</p>
          </div>
          <div class="modal-btn delete-action">
            <div class="modal-footer justify-content-center p-0">
              <button
                type="submit"
                data-bs-dismiss="modal"
                class="btn btn-primary paid-continue-btn me-2"
              >
                Yes, Delete
              </button>
              <button
                type="button"
                data-bs-dismiss="modal"
                class="btn btn-back cancel-btn"
              >
                No, Cancel
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Delete Items Modal -->
</template>
<script>
import Editor from "@tinymce/tinymce-vue";
export default {
  data() {
    return {
      content: "Description",
      content1:
        "Hi [User's Name],Welcome to Kanakku ! We're thrilled to have you on board. Get ready to experience a seamless and efficient way.To get started, Click here If you have any questions or need assistance, feel free to reach out to our support team at [support@example.com].",
    };
  },
  components: {
    editor: Editor,
  },
};
</script>
