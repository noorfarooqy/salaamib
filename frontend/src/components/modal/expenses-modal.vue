<template>
  <!-- Add Expenses Modal -->
  <div class="modal custom-modal modal-lg fade" id="add_expenses" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Expenses</h4>
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
            <div class="col-md-12">
              <div class="card-body">
                <div class="border-0 pb-0">
                  <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Expense ID</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Expense ID"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Reference</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Reference No"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Amount </label>
                        <input
                          type="number"
                          class="form-control"
                          placeholder="Enter Amount"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Payment Mode</label>
                        <vue-select
                          :options="Mode"
                          id="modepayment"
                          placeholder="Select Payment Mode"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Expense Date </label>
                        <date-picker
                          v-model="startdate"
                          class="datetimepicker form-control"
                          :editable="true"
                          :clearable="false"
                          :input-format="dateFormat"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Payment Status</label>
                        <vue-select
                          :options="Status"
                          id="statuspayment"
                          placeholder="Select Payment Status"
                        />
                      </div>
                    </div>
                    <div class="col-lg-12 col-md-12 description-box">
                      <div class="input-block mb-3" id="summernote_container">
                        <label class="form-control-label">Description</label>
                        <editor v-model="content" />
                      </div>
                    </div>
                    <div class="col-lg-12 col-md-12">
                      <div class="input-block">
                        <label>Attachment</label>
                        <div class="input-block service-upload mb-0">
                          <span
                            ><img src="@/assets/img/icons/drop-icon.svg" alt="upload"
                          /></span>
                          <h6 class="drop-browse align-center">
                            Drop your files here or<span class="text-primary ms-1"
                              >browse</span
                            >
                          </h6>
                          <p class="text-muted">Maximum size: 50MB</p>
                          <input type="file" multiple="" id="image_sign" />
                          <div id="frames"></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-primary paid-continue-btn"
            >Add Expenses</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Expenses Modal -->
  <!-- Edit Expenses Modal -->
  <div class="modal custom-modal modal-lg fade" id="edit_expenses" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Expenses</h4>
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
            <div class="col-md-12">
              <div class="card-body">
                <div class="border-0 pb-0">
                  <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Expense ID</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Expense ID"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Reference</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Reference No"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Amount </label>
                        <input
                          type="number"
                          class="form-control"
                          placeholder="Enter Amount"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Payment Mode</label>
                        <vue-select
                          :options="Mode1"
                          id="mode1"
                          placeholder="Select Payment Mode"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Expense Date </label>
                        <date-picker
                          v-model="startdateOne"
                          type="text"
                          class="datetimepicker form-control"
                          :editable="true"
                          :clearable="false"
                          placeholder="Select Expense Date"
                          :input-format="dateFormat"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Payment Status</label>
                        <vue-select
                          :options="Status1"
                          id="status1"
                          placeholder="Select Payment Mode"
                        />
                      </div>
                    </div>
                    <div class="col-lg-12 col-md-12 description-box">
                      <div class="input-block mb-3" id="summernote_container2">
                        <label class="form-control-label">Description</label>
                        <editor v-model="content" />
                      </div>
                    </div>
                    <div class="col-lg-12 col-md-12">
                      <div class="input-block">
                        <label>Attachment</label>
                        <div class="input-block service-upload mb-0">
                          <span
                            ><img src="@/assets/img/icons/drop-icon.svg" alt="upload"
                          /></span>
                          <h6 class="drop-browse align-center">
                            Drop your files here or<span class="text-primary ms-1"
                              >browse</span
                            >
                          </h6>
                          <p class="text-muted">Maximum size: 50MB</p>
                          <input type="file" multiple="" id="image_sign2" />
                          <div id="frames2"></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a
            href="javascript:;"
            data-bs-dismiss="modal"
            class="btn btn-back cancel-btn me-2"
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
  <!-- /Edit Expenses Modal -->
</template>

<script>
import Editor from "@tinymce/tinymce-vue";
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDateOne = ref(new Date());
export default {
  components: {
    editor: Editor,
  },
  data() {
    return {
      content: "Description",
      startdate: currentDate,
      startdateOne: currentDateOne,
      dateFormat: "dd-MM-yyyy",
      Mode: ["Select Payment Mode", "Cash", "Cheque"],
      Status: ["Select Payment Status", "Paid", "Pending", "Cancelled"],
      Mode1: ["Select Payment Mode", "Cash", "Cheque"],
      Status1: ["Select Payment Status", "Paid", "Pending", "Cancelled"],
    };
  },
};
</script>
