<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper add-invoice">
    <layout-header></layout-header>
    <layout-sidebar></layout-sidebar>
    <!-- Page Wrapper -->
    <div class="page-wrapper">
      <div class="content container-fluid">
        <div class="card mb-0">
          <div class="card-body">
            <div class="page-header">
              <div class="content-page-header">
                <h5>Add Invoice</h5>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12">
                <div class="form-group-item border-0 mb-0">
                  <div class="row align-item-center">
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Invoice Number</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Invoice Number"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Customer Name</label>
                        <ul class="form-group-plus css-equal-heights">
                          <li>
                            <vue-select
                              :options="Customer"
                              id="customer"
                              placeholder="Choose Customer"
                            />
                          </li>
                          <li>
                            <router-link
                              class="btn btn-primary form-plus-btn"
                              to="/customers/add-customer"
                            >
                              <i class="feather feather-plus-circle"></i>
                            </router-link>
                          </li>
                        </ul>
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Invoice Date</label>
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
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Due Date</label>
                        <div class="cal-icon cal-icon-info">
                          <date-picker
                            v-model="startdate1"
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
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Status</label>
                        <vue-select
                          :options="Status"
                          id="status4"
                          placeholder="Choose a Status"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12">
                      <div class="input-block mb-3">
                        <label>Reference Number</label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Enter Reference Number"
                        />
                      </div>
                    </div>
                    <div class="col-lg-4">
                      <div class="d-flex justify-content-between flex-wrap">
                        <div class="input-block mb-3 recurring-tab">
                          <label>Recurring</label>
                          <ul class="nav nav-pills d-flex" id="pills-tab" role="tablist">
                            <li class="nav-item" role="presentation">
                              <button
                                class="nav-link active yes"
                                id="pills-home-tab"
                                data-bs-toggle="pill"
                                data-bs-target="#pills-home"
                                type="button"
                                role="tab"
                                aria-controls="pills-home"
                                aria-selected="true"
                              >
                                Yes
                              </button>
                            </li>
                            <li class="nav-item" role="presentation">
                              <button
                                class="nav-link no"
                                id="pills-profile-tab"
                                data-bs-toggle="pill"
                                data-bs-target="#pills-profile"
                                type="button"
                                role="tab"
                                aria-controls="pills-profile"
                                aria-selected="false"
                              >
                                No
                              </button>
                            </li>
                          </ul>
                        </div>
                        <div class="tab-content pt-0" id="pills-tabContent">
                          <div
                            class="tab-pane fade show active"
                            id="pills-home"
                            role="tabpanel"
                            aria-labelledby="pills-home-tab"
                          >
                            <div class="input-block mb-3">
                              <label>Recurring cycle</label>
                              <input
                                type="text"
                                class="form-control"
                                placeholder="Enter Month"
                              />
                            </div>
                          </div>
                          <div
                            class="tab-pane fade"
                            id="pills-profile"
                            role="tabpanel"
                            aria-labelledby="pills-profile-tab"
                          ></div>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-8">
                      <div class="input-block mb-3">
                        <label>Products</label>
                        <ul class="form-group-plus css-equal-heights">
                          <li>
                            <vue-select
                              :options="Product"
                              id="producttwo"
                              placeholder="Select Product"
                            />
                          </li>
                          <li>
                            <router-link
                              class="btn btn-primary form-plus-btn"
                              to="/product-service/add-products"
                            >
                              <i class="feather feather-plus-circle"></i>
                            </router-link>
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="form-group-item mt-3">
                  <div class="card-table">
                    <div class="card-body">
                      <div class="table-responsive no-pagination">
                        <a-table
                          class="stripped table-hover"
                          :columns="columns"
                          :data-source="data"
                        >
                          <template #bodyCell="{ column }">
                            <template v-if="column.key === 'id'">
                              <input type="number" class="form-control" value="0" />
                            </template>
                            <template v-else-if="column.key === 'rate'">
                              <input
                                type="number"
                                class="form-control"
                                placeholder="120"
                              />
                            </template>
                            <template v-else-if="column.key === 'action'">
                              <div class="d-flex align-items-center">
                                <a
                                  href="javascript:;"
                                  class="btn-action-icon me-2"
                                  data-bs-toggle="modal"
                                  data-bs-target="#add_discount"
                                  ><span><i class="feather feather-edit"></i></span
                                ></a>
                                <a
                                  href="javascript:;"
                                  class="btn-action-icon"
                                  data-bs-toggle="modal"
                                  data-bs-target="#delete_discount"
                                  ><span><i class="feather feather-trash-2"></i></span
                                ></a>
                              </div>
                            </template>
                          </template>
                        </a-table>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-4">
                    <div class="row">
                      <div class="col-lg-7">
                        <div class="form-group">
                          <label>Discount Type</label>
                          <vue-select
                            :options="Percentage"
                            id="percentageone"
                            placeholder="Percentage(%)"
                          />
                        </div>
                      </div>
                      <div class="col-lg-5">
                        <div class="form-group">
                          <label>Discount(%)</label>
                          <input type="text" class="form-control" placeholder="10" />
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-4">
                    <div class="form-group">
                      <label>Tax</label>
                      <vue-select :options="Tax" id="invoice-tax" placeholder="No Tax" />
                    </div>
                  </div>
                  <div class="col-md-4"></div>
                </div>
                <div class="form-group-item border-0 p-0 mt-4">
                  <div class="row">
                    <div class="col-xl-6 col-lg-12">
                      <div class="form-group-bank">
                        <div class="row align-items-center">
                          <div class="col-md-8">
                            <div class="input-block mb-3">
                              <label>Select Bank</label>
                              <vue-select
                                :options="Bank"
                                id="bank7"
                                placeholder="Select Bank"
                              />
                            </div>
                          </div>
                          <div class="col-md-4">
                            <div class="form-groups">
                              <a
                                class="btn btn-primary"
                                href="javascript:;"
                                data-bs-toggle="modal"
                                data-bs-target="#bank_details"
                                >Add Bank</a
                              >
                            </div>
                          </div>
                        </div>

                        <div class="input-block mb-3 notes-form-group-info">
                          <label>Notes</label>
                          <textarea
                            class="form-control"
                            placeholder="Enter Notes"
                          ></textarea>
                        </div>
                        <div class="input-block notes-form-group-info mb-0">
                          <label>Terms and Conditions</label>
                          <textarea
                            class="form-control"
                            placeholder="Enter Terms and Conditions"
                          ></textarea>
                        </div>
                      </div>
                    </div>
                    <div class="col-xl-6 col-lg-12">
                      <div class="form-group-bank">
                        <div class="invoice-total-box">
                          <div class="invoice-total-inner">
                            <p>Taxable Amount <span>$120.00</span></p>
                            <p>Discount <span>$13.20</span></p>
                            <p>Vat <span>$0.00</span></p>
                            <div class="status-toggle justify-content-between">
                              <div class="d-flex align-center">
                                <p>Round Off</p>
                                <input
                                  id="rating_1"
                                  class="check"
                                  type="checkbox"
                                  checked=""
                                />
                                <label for="rating_1" class="checktoggle checkbox-bg"
                                  >checkbox</label
                                >
                              </div>
                              <span>$0.00</span>
                            </div>
                          </div>
                          <div class="invoice-total-footer">
                            <h4>Total Amount <span>$107.80</span></h4>
                          </div>
                        </div>
                        <div class="form-group mt-3">
                          <label>Signature Name</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Enter Signature Name"
                          />
                        </div>
                        <div class="form-group mb-0 mt-3">
                          <label>Signature Image</label>
                          <div class="form-group service-upload service-upload-info mb-0">
                            <span
                              ><i class="feather feather-upload-cloud me-1"></i>Upload
                              Signature</span
                            >
                            <input type="file" multiple="" id="image_sign" />
                            <div id="frames"></div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <form @submit.prevent="submitForm" class="add-customer-btns text-end">
                  <button type="reset" class="btn btn-primary cancel me-2">Cancel</button>
                  <button type="reset" class="btn btn-primary cancel me-2">Save</button>
                  <button type="submit" class="btn btn-primary">Save & Send</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- /Page Wrapper -->
    <locationmodal :Delete="Delete" />
  </div>
  <!-- /Main Wrapper -->
</template>
<script>
const columns = [
  {
    title: "Product / Service",
    dataIndex: "Product",
    sorter: {
      compare: (a, b) => {
        a = a.Product.toLowerCase();
        b = b.Product.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Quantity",
    dataIndex: "Quantity",
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.Quantity.toLowerCase();
        b = b.Quantity.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Unit",
    dataIndex: "Unit",
    sorter: {
      compare: (a, b) => {
        a = a.CategoryName.toLowerCase();
        b = b.CategoryName.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Rate",
    dataIndex: "Rate",
    key: "rate",
    sorter: {
      compare: (a, b) => {
        a = a.Rate.toLowerCase();
        b = b.Rate.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Discount",
    dataIndex: "Discount",
    sorter: {
      compare: (a, b) => {
        a = a.Discount.toLowerCase();
        b = b.Discount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Tax",
    dataIndex: "Tax",
    sorter: {
      compare: (a, b) => {
        a = a.Tax.toLowerCase();
        b = b.Tax.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Amount",
    dataIndex: "Amount",
    sorter: {
      compare: (a, b) => {
        a = a.Amount.toLowerCase();
        b = b.Amount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Action",
    key: "action",
    sorter: true,
  },
];
const data = [
  {
    Product: "Lorem ipsum dolor sit amet",
    Unit: "Pcs",
    Rate: "$120.00",
    Discount: "0",
    Tax: "0",
    Amount: "$120.00",
  },
];
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDateOne = ref(new Date());
export default {
  data() {
    return {
      startdate: currentDate,
      dateFormat: "dd-MM-yyyy",
      startdate1: currentDateOne,
      Delete: "Delete Product / Services",
      title: "Add Invoice",
      Customer: ["Choose Customer", "Customer 1", "Customer 2", "Customer 3"],
      GST: ["Without GST", "With GST"],
      Product: ["Select Product", "Product 1", "Product 2", "Product 3"],
      Percentage: ["Percentage(%)", "0%", "5%", "10%", "15%"],
      Currency: ["Select Currency", "US dollar", "Euro", "Pound sterling", "Swiss franc"],
      Status: [
        "Choose a Status",
        "Unpaid",
        "Partially paid",
        "Paid",
        "Overdue",
        "Cancelled",
        "Refunded",
        "Draft",
      ],
      cycle: [
        "Choose a Recurring cycle",
        "Monthly",
        "Quarterly",
        "Semi annually",
        "Annually",
      ],
      Tax: ["No Tax", "IVA - (21%)", "IRPF - (-15%)", "PDV - (20%)"],
      Bank: ["Select Bank", "SBI", "IOB", "Canara"],
      data,
      columns,
    };
  },
  mounted() {
    document.addEventListener("DOMContentLoaded", function () {
      const imageSign = document.querySelector("#image_sign");
      imageSign.addEventListener("change", function () {
        const frames = document.querySelector("#frames");
        frames.innerHTML = "";
        for (let i = 0; i < this.files.length; i++) {
          const img = document.createElement("img");
          img.src = window.URL.createObjectURL(this.files[i]);
          img.width = "100";
          img.height = "100";
          frames.appendChild(img);
        }
      });
    });
  },
  methods: {
    submitForm() {
      this.$router.push("/invoices");
    },
  },
};
</script>
