<template>
  <div class="modal custom-modal fade" id="add_ticket" role="dialog">
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
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Subject</label>
                <input type="text" class="form-control" placeholder="Enter Subject" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Assigned Name</label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter Assigned Name"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Assigned Date</label>
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

            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Due Date</label>
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
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Assignee Name</label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter Assignee Name"
                />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="input-block mb-3">
                <label>Priority</label>
                <vue-select
                  :options="Priority"
                  id="priority"
                  placeholder="Select Priority"
                />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="input-block mb-0">
                <label>Status</label>
                <vue-select :options="Status" id="status" placeholder="Select Status" />
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

  <!-- Edit Ticket Modal -->
  <div class="modal custom-modal fade" id="edit_ticket" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Ticket</h4>
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
                <label>Subject</label>
                <input
                  type="text"
                  class="form-control"
                  value="Support for theme"
                  placeholder="Enter Subject"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Assigned Name</label>
                <input
                  type="text"
                  class="form-control"
                  value="Richard"
                  placeholder="Enter Assigned Name"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Assigned Date</label>
                <div class="cal-icon cal-icon-info">
                  <date-picker
                    v-model="startdateTwo"
                    type="text"
                    class="datetimepicker form-control"
                    :editable="true"
                    :clearable="false"
                    :input-format="dateFormat"
                    placeholder="Select Date"
                    value="17 Dec 2023"
                  />
                  <i class="feather feather-calendar calendar-icon"></i>
                </div>
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Created Date</label>
                <div class="cal-icon cal-icon-info">
                  <date-picker
                    v-model="startdate1"
                    type="text"
                    class="datetimepicker form-control"
                    :editable="true"
                    :clearable="false"
                    :input-format="dateFormat"
                    placeholder="Select Date"
                    value="17 Dec 2023"
                  />
                  <i class="feather feather-calendar calendar-icon"></i>
                </div>
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Due Date</label>
                <div class="cal-icon cal-icon-info">
                  <date-picker
                    v-model="startdate2"
                    type="text"
                    class="datetimepicker form-control"
                    :editable="true"
                    :clearable="false"
                    :input-format="dateFormat"
                    placeholder="Select Date"
                    value="17 Dec 2023"
                  /><i class="feather feather-calendar calendar-icon"></i>
                </div>
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Assignee Name</label>
                <input
                  type="text"
                  class="form-control"
                  value="John Smith"
                  placeholder="Enter Assignee Name"
                />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="input-block mb-3">
                <label>Priority</label>
                <vue-select
                  :options="Priority1"
                  id="priority1"
                  placeholder="Select Priority"
                />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="input-block mb-0">
                <label>Status</label>
                <vue-select :options="Status1" id="Status1" placeholder="Select Status" />
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
</template>
<script>
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDateOne = ref(new Date());
const currentDateTwo = ref(new Date());
const currentDate1 = ref(new Date());
const currentDate2 = ref(new Date());
export default {
  setup() {
    return {
      startdate: currentDate,
      startdateOne: currentDateOne,
      startdateTwo: currentDateTwo,
      startdate1: currentDate1,
      startdate2: currentDate2,
      dateFormat: "dd-MM-yyyy",
      Priority: ["Select Priority", "Priority 1", "Priority 2", "Priority 3"],
      Priority1: ["Select Priority", "Medium", "Low", "High"],
      Status: ["Select Status", "Status 1", "Status 2", "Status 3"],
      Status1: ["Select Status", "Resolved", "Pending", "Closed"],
    };
  },
};
</script>
