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
                <h5>Add Credit Note</h5>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12">
                <div class="cards">
                  <div class="form-group-item border-0 mb-0">
                    <div class="row align-item-center">
                      <div class="col-lg-4 col-md-6 col-sm-12">
                        <div class="input-block mb-3">
                          <label>Credit Notes Id</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Enter Credit Note ID"
                          />
                        </div>
                      </div>
                      <div class="col-lg-4 col-md-6 col-sm-12">
                        <div class="input-block mb-3">
                          <label>Select Customer</label>
                          <ul class="form-group-plus css-equal-heights">
                            <li>
                              <vue-select
                                :options="Customer"
                                id="addcustomer"
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
                          <label>Credit Note Date</label>
                          <div class="cal-icon cal-icon-info">
                            <date-picker
                              v-model="startdate"
                              class="datetimepicker form-control"
                              :editable="true"
                              :clearable="false"
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
                              v-model="startdateOne"
                              class="datetimepicker form-control"
                              :editable="true"
                              :clearable="false"
                              :input-format="dateFormat"
                            />
                            <i class="feather feather-calendar calendar-icon"></i>
                          </div>
                        </div>
                      </div>
                      <div class="col-lg-4 col-md-6 col-sm-12">
                        <div class="input-block mb-3">
                          <label>Reference No</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Enter Reference Number"
                          />
                        </div>
                      </div>
                      <div class="col-lg-12">
                        <div class="input-block mb-3">
                          <label>Products</label>
                          <ul class="form-group-plus css-equal-heights">
                            <li>
                              <vue-select
                                :options="Product"
                                id="productfour"
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
                  <div class="form-group-item">
                    <div class="card-table">
                      <div class="card-body">
                        <div class="table-responsive no-pagination">
                          <a-table
                            class="stripped table-hover"
                            :columns="columns"
                            :data-source="data"
                          >
                            <template #bodyCell="{ column }">
                              <template v-if="column.key === 'Quantity'">
                                <input
                                  type="number"
                                  class="form-control"
                                  placeholder="0"
                                />
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
                          <div class="input-block mb-3">
                            <label>Discount Type</label>
                            <vue-select
                              :options="Percentages"
                              id="addtype"
                              placeholder="Percentage(%)"
                            />
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
                        <vue-select :options="Tax" id="taxcredit" placeholder="No Tax" />
                      </div>
                    </div>
                    <div class="col-md-4"></div>
                  </div>
                  <div class="form-group-item border-0 p-0">
                    <div class="row">
                      <div class="col-xl-6 col-lg-12">
                        <div class="form-group-bank">
                          <div class="row align-items-center">
                            <div class="col-md-8">
                              <div class="input-block mb-3">
                                <label>Select Bank</label>
                                <vue-select
                                  :options="Bank"
                                  id="creditbank"
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
                          <div class="input-block mb-3 notes-form-group-info mb-0">
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
                          <div class="input-block mb-3">
                            <label>Signature Name</label>
                            <input
                              type="text"
                              class="form-control"
                              placeholder="Enter Signature Name"
                            />
                          </div>
                          <div class="input-block mb-0">
                            <label>Signature Image</label>
                            <div
                              class="input-block mb-3 service-upload service-upload-info mb-0"
                            >
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
                  <div class="add-customer-btns text-end">
                    <router-link to="credit-notes" class="btn customer-btn-cancel"
                      >Cancel</router-link
                    >
                    <router-link to="credit-notes" class="btn customer-btn-save"
                      >Save</router-link
                    >
                  </div>
                </div>
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
    key: "Quantity",
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
        a = a.Unit.toLowerCase();
        b = b.Unit.toLowerCase();
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
    Quantity: "0",
    Unit: "Pcs",
    Rate: "$120.00",
    Discount: "0",
    Tax: "0",
    Amount: "$120.00",
    Action: "",
  },
];
import { ref } from "vue";
const currentDate = ref(new Date());
const currentDateOne = ref(new Date());
export default {
  data() {
    return {
      startdate: currentDate,
      startdateOne: currentDateOne,
      dateFormat: "dd-MM-yyyy",
      title: "Add Credit Note",
      Delete: "Delete Product / Services",
      Customer: ["Choose Customer", "Customer 1", "Customer 2", "Customer 3"],
      GST: ["Without GST", "With GST"],
      Product: ["Select Product", "Product 1", "Product 2", "Product 3"],
      Percentage: ["Percentage(%)", "0%", "5%", "10%", "15%"],
      Currency: ["Select Currency", "US dollar", "Euro", "Pound sterling", "Swiss franc"],
      Bank: ["Select Bank", "SBI", "IOB", "Canara"],
      Tax: ["NoTax", "IVA - (21%)", "IRPF - (-15%)", "PDV - (20%)"],
      Percentages: ["Percentage(%)", "Fixed"],
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
};
</script>
