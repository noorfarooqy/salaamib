<template>
  <!-- Add Ticket Modal -->
  <div class="modal custom-modal modal-lg fade" id="add_ticket" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Ticket</h4>
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
            <div class="col-lg-4 col-md-12">
              <div class="input-block mb-3">
                <label>Subject</label>
                <input type="text" class="form-control" placeholder="Enter Subject" />
              </div>
            </div>
            <div class="col-lg-4 col-md-12">
              <div class="input-block mb-3">
                <label>Assigned Name</label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter Assigned Name"
                />
              </div>
            </div>
            <div class="col-lg-4 col-md-12">
              <div class="input-block mb-3">
                <label>Assigned Date</label>
                <div class="cal-icon">
                  <date-picker
                    v-model="startdateOne"
                    placeholder="Choose Date"
                    class="datetimepicker form-control"
                    :editable="true"
                    :clearable="false"
                    :input-format="dateFormat"
                  />
                </div>
              </div>
            </div>
            <div class="col-lg-4 col-md-12">
              <div class="input-block mb-3">
                <label>Created Date</label>
                <div class="cal-icon">
                  <date-picker
                    v-model="startdateTwo"
                    placeholder="Choose Date"
                    class="datetimepicker form-control"
                    :editable="true"
                    :clearable="false"
                    :input-format="dateFormat"
                  />
                </div>
              </div>
            </div>
            <div class="col-lg-4 col-md-12">
              <div class="input-block mb-3">
                <label>Due Date</label>
                <div class="cal-icon">
                  <date-picker
                    v-model="startdate"
                    placeholder="Choose Date"
                    class="datetimepicker form-control"
                    :editable="true"
                    :clearable="false"
                    :input-format="dateFormat"
                  />
                </div>
              </div>
            </div>
            <div class="col-lg-4 col-md-12">
              <div class="input-block mb-3">
                <label>Assignee Name</label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter Assignee Name"
                />
              </div>
            </div>
            <div class="col-lg-4">
              <div class="input-block mb-0">
                <label>Priority</label>
                <vue-select
                  :options="Priority"
                  id="priority"
                  placeholder="Select Priority"
                />
              </div>
            </div>
            <div class="col-lg-4">
              <div class="input-block mb-0">
                <label>Status</label>
                <vue-select :options="Status" id="status9" placeholder="Select Status" />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Save</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Ticket Modal -->
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
          >
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
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
              <div class="form-group">
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
              <div class="form-group">
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
              <div class="form-group">
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
              <div class="form-group mb-0">
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
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Update</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Vendor Modal -->

  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade" id="delete_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>Delete Contact Messages</h3>
            <p>Are you sure want to delete?</p>
          </div>
          <div class="modal-btn delete-action">
            <div class="row">
              <div class="col-6">
                <button
                  type="reset"
                  data-bs-dismiss="modal"
                  class="w-100 btn btn-primary paid-continue-btn"
                >
                  Delete
                </button>
              </div>
              <div class="col-6">
                <button
                  type="submit"
                  data-bs-dismiss="modal"
                  class="w-100 btn btn-primary paid-cancel-btn"
                >
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Delete Items Modal -->
  <!-- Edit Role Modal -->
  <div class="modal custom-modal fade" id="edit_role" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Role</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group mb-0">
                <label>Role Name <span class="text-danger">*</span></label>
                <input
                  type="text"
                  class="form-control"
                  Value="Admin"
                  placeholder="Enter Role Name"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Close</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Submit</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Role Modal -->
  <!-- Add Role Modal -->
  <div class="modal custom-modal fade" id="add_role" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Role</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <span class="align-center" aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <div class="form-group mb-0">
                <label>Role Name <span class="text-danger">*</span></label>
                <input type="text" class="form-control" placeholder="Enter Role Name" />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-cancel-btn me-2"
            >Close</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Submit</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Role Modal -->
</template>
<script>
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDateOne = ref(new Date());
const currentDateTwo = ref(new Date());
export default {
  setup() {
    return {
      startdate: currentDate,
      startdateOne: currentDateOne,
      startdateTwo: currentDateTwo,
      dateFormat: "dd-MM-yyyy",
      Priority: ["Select Priority", "Priority 1", "Priority 2", "Priority 3"],
      Status: ["Select Status", "Status 1", "Status 2", "Status 3"],
    };
  },
};
</script>
