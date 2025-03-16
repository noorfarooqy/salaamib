<template>
  <!-- Add Ledger Modal -->
  <div class="modal custom-modal fade" id="add_ledger" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Ledger</h4>
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
                <label>Amount</label>
                <input type="text" class="form-control" placeholder="Enter Amount" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Date</label>
                <div class="cal-icon cal-icon-info">
                  <date-picker
                    v-model="startdate"
                    class="datetimepicker form-control"
                    :editable="true"
                    :clearable="false"
                    placeholder="Select Date"
                    :input-format="dateFormat"
                  />
                  <i class="feather feather-calendar calendar-icon"></i>
                </div>
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block d-inline-flex align-center mb-0">
                <label class="me-5 mb-0">Mode</label>
                <div>
                  <label class="custom_radio me-3 mb-0">
                    <input type="radio" name="payment" checked />
                    <span class="checkmark"></span> Credit
                  </label>
                  <label class="custom_radio mb-0">
                    <input type="radio" name="payment" />
                    <span class="checkmark"></span> Debit
                  </label>
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
            >Submit</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Ledger Modal -->

  <!-- Edit Ledger Modal -->
  <div class="modal custom-modal fade" id="edit_ledger" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Ledger</h4>
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
                <label>Amount</label>
                <input type="text" class="form-control" placeholder="$300" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block mb-3">
                <label>Date</label>
                <div class="cal-icon cal-icon-info">
                  <date-picker
                    v-model="startdateOne"
                    class="datetimepicker form-control"
                    :editable="true"
                    :clearable="false"
                    placeholder="16 Aug 2023, 06:12 PM"
                    :input-format="dateFormat"
                  />
                  <i class="feather feather-calendar calendar-icon"></i>
                </div>
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="input-block d-inline-flex align-center mb-0">
                <label class="me-5 mb-0">Mode</label>
                <div>
                  <label class="custom_radio me-3 mb-0">
                    <input type="radio" name="payment" checked />
                    <span class="checkmark"></span> Credit
                  </label>
                  <label class="custom_radio mb-0">
                    <input type="radio" name="payment" />
                    <span class="checkmark"></span> Debit
                  </label>
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
            >Submit</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Edit Ledger Modal -->
</template>

<script>
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDateOne = ref(new Date());
export default {
  data() {
    return {
      startdate: currentDate,
      startdateOne: currentDateOne,
      dateFormat: "dd-MM-yyyy",      
    };
  },
};
</script>
