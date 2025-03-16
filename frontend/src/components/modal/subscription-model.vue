<template>
  <!-- Edit Vendor Modal -->
  <div class="modal custom-modal fade" id="edit_contact" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Contact Messages</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Name</label>
                <input
                  type="text"
                  class="form-control"
                  value="John Smith"
                  placeholder="Enter Name"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Email</label>
                <input
                  type="text"
                  class="form-control"
                  value="john@example.com"
                  placeholder="Email"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Mobile</label>
                <input
                  type="text"
                  class="form-control"
                  value="989-438-3131"
                  placeholder="Enter Mobile Number"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Message</label>
                <input
                  type="text"
                  class="form-control"
                  value="Lorem ipsum dolor"
                  placeholder="message"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-0">
                <label>Date</label>
                <input
                  type="text"
                  class="form-control"
                  value="15 Dec 2023, 04:35 PM"
                  placeholder="message"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a href="#" data-bs-dismiss="modal" class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a href="#" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Vendor Modal -->

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
            <p>You want delete plan</p>
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
