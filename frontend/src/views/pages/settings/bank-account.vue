<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="row">
        <div class="col-xl-3 col-md-4">
          <settingsidebar />
        </div>
        <div class="col-xl-9 col-md-8">
          <div class="card">
            <div class="card-body w-100">
              <div class="content-page-header p-0">
                <h5>Bank Accounts</h5>
                <div class="list-btn">
                  <a
                    href="javascript:;"
                    class="btn btn-primary"
                    data-bs-toggle="modal"
                    data-bs-target="#bank_details"
                    ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i>Add Bank</a
                  >
                </div>
              </div>
              <div class="row">
                <div class="col-sm-12">
                  <div class="card-table">
                    <div class="card-body">
                      <div class="table-responsive no-pagination">
                        <a-table
                          class="stripped table-center table-hover"
                          :columns="columns"
                          :data-source="data"
                        >
                          <template #bodyCell="{ column, record }">
                            <template v-if="column.key === 'id'">
                              <h2 class="table-avatar d-flex">
                                <router-link to="/profile">{{ record.Name }}</router-link>
                              </h2>
                            </template>
                            <template v-else-if="column.key === 'Action'">
                              <div class="d-flex align-items-center">
                                <div class="dropdown dropdown-action">
                                  <a
                                    href="javascript:;"
                                    class="btn-action-icon"
                                    data-bs-toggle="dropdown"
                                    aria-expanded="false"
                                    ><i class="fas fa-ellipsis-v"></i
                                  ></a>
                                  <div class="dropdown-menu dropdown-menu-end">
                                    <ul>
                                      <li>
                                        <a
                                          class="dropdown-item"
                                          href="javascript:void(0);"
                                          ><i class="far fa-edit me-2"></i>Edit</a
                                        >
                                      </li>
                                      <li>
                                        <a
                                          class="dropdown-item"
                                          href="javascript:void(0);"
                                          data-bs-toggle="modal"
                                          data-bs-target="#delete_modal"
                                          ><i class="far fa-trash-alt me-2"></i>Delete</a
                                        >
                                      </li>
                                      <li>
                                        <a
                                          class="dropdown-item"
                                          href="javascript:void(0);"
                                          ><i class="far fa-eye me-2"></i>View</a
                                        >
                                      </li>
                                    </ul>
                                  </div>
                                </div>
                              </div>
                            </template>
                          </template>
                        </a-table>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
  <!-- Delete Items Modal -->
  <div class="modal custom-modal fade" id="delete_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>Delete Account Details</h3>
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

  <!-- Add Bank Details Modal -->
  <div class="modal custom-modal fade" id="bank_details" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Bank Details</h4>
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
                <label>Bank Name <span class="text-danger">*</span></label>
                <input type="text" class="form-control" placeholder="Enter Bank Name" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Account Number <span class="text-danger">*</span></label>
                <input
                  type="number"
                  class="form-control"
                  placeholder="Enter Account Number"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Account Holder Name <span class="text-danger">*</span></label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter Account Holder Name"
                />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <label>Branch Name <span class="text-danger">*</span></label>
                <input type="text" class="form-control" placeholder="Enter Branch Name" />
              </div>
            </div>
            <div class="col-lg-12 col-md-12">
              <div class="form-group mb-0">
                <label>IFSC Code <span class="text-danger">*</span></label>
                <input type="number" class="form-control" placeholder="Enter IFSC COde" />
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
  <!-- /Add Bank Details Modal -->
</template>
<script>
const columns = [
  {
    title: "#",
    dataIndex: "num",
    sorter: {
      compare: (a, b) => {
        a = a.num.toLowerCase();
        b = b.num.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Name",
    dataIndex: "Name",
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.Name.toLowerCase();
        b = b.Name.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Bank Name",
    dataIndex: "BankName",
    sorter: {
      compare: (a, b) => {
        a = a.BankName.toLowerCase();
        b = b.BankName.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Branch",
    dataIndex: "Branch",
    sorter: {
      compare: (a, b) => {
        a = a.Branch.toLowerCase();
        b = b.Branch.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Account Number",
    dataIndex: "AccountNumber",
    sorter: {
      compare: (a, b) => {
        a = a.AccountNumber.toLowerCase();
        b = b.AccountNumber.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "IFSC Code",
    dataIndex: "IFSCCode",
    sorter: {
      compare: (a, b) => {
        a = a.IFSCCode.toLowerCase();
        b = b.IFSCCode.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Action",
    key: "Action",
    sorter: true,
  },
];
const data = [
  {
    num: "1",
    Name: "John Smith",
    BankName: "Axis Bank",
    Branch: "Adambakkam",
    AccountNumber: "123 456 78920",
    IFSCCode: "UTIB0003259",
  },
  {
    num: "2",
    Name: "Johnny",
    BankName: "Bank of India",
    Branch: "Adyar",
    AccountNumber: "756 890 65820",
    IFSCCode: "BKID0008010",
  },
  {
    num: "3",
    Name: "Robert",
    BankName: "Canara Bank",
    Branch: "Karavalur",
    AccountNumber: "756 890 75689",
    IFSCCode: "CNRB0001483",
  },
  {
    num: "4",
    Name: "Sharonda",
    BankName: "ICICI Bank",
    Branch: "Vadavalli",
    AccountNumber: "756 890 36586",
    IFSCCode: "ICIC0002142",
  },
  {
    num: "5",
    Name: "Pricilla",
    BankName: "Karur Vysya Bank",
    Branch: "Chennai",
    AccountNumber: "756 890 88669",
    IFSCCode: "KVBL0001153",
  },
  {
    num: "6",
    Name: "Randall",
    BankName: "State Bank of India",
    Branch: "Chennai",
    AccountNumber: "756 890 36589",
    IFSCCode: "SBIN0000800",
  },
];
export default {
  setup() {
    return {
      data,
      columns,
    };
  },
};
</script>
