<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="signature-invoice">
        <div class="page-header">
          <div class="content-page-header">
            <h5>Create Invoice</h5>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <div class="edit-card">
              <div class="card-body">
                <div class="form-group-item border-0 mb-0">
                  <div class="row align-item-center">
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Invoice Number</label>
                        <input type="text" class="form-control" placeholder="Enter Invoice Number" />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Customer Name</label>
                        <ul class="form-group-plus css-equal-heights">
                          <li>
                            <vue-select :options="Customer" id="name" placeholder="Customer 1" />
                          </li>
                          <li>
                            <router-link class="btn btn-primary form-plus-btn" to="/customers/add-customer">
                              <i class="feather feather-plus-circle"></i>
                            </router-link>
                          </li>
                        </ul>
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Invoice Date</label>
                        <div class="cal-icon">
                          <date-picker v-model="startdate" class="datetimepicker form-control" :editable="true"
                            :clearable="false" :input-format="dateFormat" />
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Due Date</label>
                        <div class="cal-icon">
                          <date-picker v-model="startdateOne" class="datetimepicker form-control" :editable="true"
                            :clearable="false" :input-format="dateFormat" />
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Status</label>
                        <vue-select :options="Status" id="status8" placeholder="Unpaid" />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Reference Number</label>
                        <input type="text" class="form-control" placeholder="Enter Reference Number" />
                      </div>
                    </div>
                    <div class="col-lg-4">
                      <div class="d-flex justify-content-between flex-wrap">
                        <div class="input-block mb-3 recurring-tab">
                          <label>Recurring</label>
                          <ul class="nav nav-pills d-flex" id="pills-tab" role="tablist">
                            <li class="nav-item" role="presentation">
                              <button class="nav-link active yes" id="pills-home-tab" data-bs-toggle="pill"
                                data-bs-target="#pills-home" type="button" role="tab" aria-controls="pills-home"
                                aria-selected="true">
                                Yes
                              </button>
                            </li>
                            <li class="nav-item" role="presentation">
                              <button class="nav-link no" id="pills-profile-tab" data-bs-toggle="pill"
                                data-bs-target="#pills-profile" type="button" role="tab" aria-controls="pills-profile"
                                aria-selected="false">
                                No
                              </button>
                            </li>
                          </ul>
                        </div>
                        <div class="tab-content pt-0" id="pills-tabContent">
                          <div class="tab-pane fade show active" id="pills-home" role="tabpanel"
                            aria-labelledby="pills-home-tab">
                            <div class="input-block mb-3">
                              <label>Recurring cycle</label>
                              <input type="text" class="form-control" placeholder="Enter Month" />
                            </div>
                          </div>
                          <div class="tab-pane fade" id="pills-profile" role="tabpanel"
                            aria-labelledby="pills-profile-tab"></div>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-8">
                      <div class="input-block mb-3">
                        <label>Products</label>
                        <ul class="form-group-plus css-equal-heights">
                          <li>
                            <vue-select :options="Product" id="productseven" placeholder="Product" />
                          </li>
                          <li>
                            <router-link class="btn btn-primary form-plus-btn" to="/product-service/add-products">
                              <i class="feather feather-plus-circle"></i>
                            </router-link>
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="form-group-item">
                  <div class="card-table">
                    <div class="card-body">
                      <div class="table-responsive">
                        <signature-table />
                      </div>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-4">
                    <div class="row">
                      <div class="col-lg-7">
                        <div class="input-block mb-3">
                          <label>Discount Type</label>
                          <vue-select :options="Discount" id="type" placeholder="Percentage(%)" />
                        </div>
                      </div>
                      <div class="col-lg-5">
                        <div class="input-block mb-3">
                          <label>Discount(%)</label>
                          <input type="text" class="form-control" placeholder="10" />
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-4">
                    <div class="input-block mb-3">
                      <label>Tax</label>
                      <vue-select :options="Tax" id="tax-signature" placeholder="No Tax" />
                    </div>
                  </div>
                  <div class="col-md-4"></div>
                </div>
                <div class="form-group-item border-0 p-0">
                  <div class="row">
                    <selectbank></selectbank>
                  </div>
                </div>
                <div class="preview-boxs">
                  <router-link to="/signature/signature-preview-invoice">Preview Invoice</router-link>
                  <form @submit.prevent="submitForm" class="add-customer-btns text-end">
                    <button type="reset" class="btn btn-primary cancel me-2">
                      Cancel
                    </button>
                    <button type="reset" class="btn btn-primary cancel me-2">
                      Save
                    </button>
                    <button type="submit" class="btn btn-primary">Save & Send</button>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
  <signature-model />
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
      Customer: ["Customer 1", "Customer 2", "Customer 3"],
      Discount: ["Percentage(%)", "Fixed"],
      Tax: ["No Tax", "IVA - (21%)", "IRPF - (-15%)", "PDV - (20%)"],
      Product: ["Product 1", "Product 2", "Product 3"],
      Status: [
        "Unpaid",
        "Partially paid",
        "Paid",
        "Overdue",
        "Cancelled",
        "Refunded",
        "Draft",
      ],
    };
  },
  methods: {
    submitForm() {
      this.$router.push("/invoices");
    },
  },
};
</script>
