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
                <h5>Tax Rates</h5>
                <div class="list-btn">
                  <a href="javascript:;" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#add_discount"><i
                      class="fa fa-plus-circle me-2" aria-hidden="true"></i>Add Tax</a>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-12">
                  <div class="card-table">
                    <div class="card-body">
                      <div class="table-responsive no-pagination">
                        <a-table class="stripped table-center table-hover" :columns="columns" :data-source="data">
                          <template #bodyCell="{ column, record }">
                            <template v-if="column.key === 'id'">
                              <h2 class="tax-name">{{ record.Name }}</h2>
                            </template>
                            <template v-else-if="column.key === 'Status'">
                              <div class="status-toggle">
                                <input :id="record.id" class="check" type="checkbox" checked="" />
                                <label :for="record.For" class="checktoggle checkbox-bg">{{ record.Status }}</label>
                              </div>
                            </template>
                            <template v-else-if="column.key === 'Action'">
                              <div class="d-flex align-items-center">
                                <div class="dropdown dropdown-action">
                                  <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown"
                                    aria-expanded="false"><i class="fas fa-ellipsis-v"></i></a>
                                  <div class="dropdown-menu dropdown-menu-end">
                                    <ul>
                                      <li>
                                        <a class="dropdown-item" href="javascript:void(0);"><i
                                            class="far fa-edit me-2"></i>Edit</a>
                                      </li>
                                      <li>
                                        <a class="dropdown-item" href="javascript:void(0);"><i
                                            class="far fa-trash-alt me-2"></i>Delete</a>
                                      </li>
                                      <li>
                                        <a class="dropdown-item" href="javascript:void(0);"><i
                                            class="far fa-eye me-2"></i>View</a>
                                      </li>
                                    </ul>
                                  </div>
                                </div>
                              </div>
                            </template>
                          </template>
                        </a-table>
                        <div class="col-lg-12">
                          <div class="btn-path text-end">
                            <a href="javascript:void(0);" class="btn btn-cancel bg-primary-light me-3">Cancel</a>
                            <a href="javascript:void(0);" class="btn btn-primary">Save Changes</a>
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
    </div>
  </div>
  <taxratsmodel></taxratsmodel>
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
    title: "Tax Rate",
    dataIndex: "TaxRate",
    sorter: {
      compare: (a, b) => {
        a = a.TaxRate.toLowerCase();
        b = b.TaxRate.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Status",
    dataIndex: "Status",
    key: "Status",
    sorter: {
      compare: (a, b) => {
        a = a.Status.toLowerCase();
        b = b.Status.toLowerCase();
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
    Name: "VAT@10%",
    TaxRate: "10.00",
    Status: "checkbox",
    id: "rating_1",
    For: "rating_1",
  },
  {
    num: "2",
    Name: "GST@10",
    TaxRate: "10.00",
    Status: "checkbox",
    id: "rating_2",
    For: "rating_2",
  },
  {
    num: "3",
    Name: "VAT@5%",
    TaxRate: "5.00",
    Status: "checkbox",
    id: "rating_3",
    For: "rating_3",
  },
  {
    num: "4",
    Name: "GST@5",
    TaxRate: "5.00",
    Status: "checkbox",
    id: "rating_4",
    For: "rating_4",
  },
  {
    num: "5",
    Name: "VAT@15%",
    TaxRate: "15.00",
    Status: "checkbox",
    id: "rating_5",
    For: "rating_5",
  },
  {
    num: "6",
    Name: "GST@15",
    TaxRate: "15.00",
    Status: "checkbox",
    id: "rating_6",
    For: "rating_6",
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
