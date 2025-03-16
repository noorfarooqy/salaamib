<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <div class="page-header">
        <div class="content-page-header">
          <h5>Signature</h5>
          <div class="list-btn">
            <ul class="filter-list">
              <li>
                <a class="btn btn-primary" href="javascript:void(0);" data-bs-toggle="modal"
                  data-bs-target="#add_modal"><i class="fa fa-plus-circle me-2" aria-hidden="true"></i>Add
                  Signature</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <!-- /Page Header -->

      <!-- Table -->
      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'Name'">
                      <div class="table-avatar d-flex">
                        <img class="img-fluid" width="80" height="30" :src="require(`@/assets/img/${record.Signature}`)"
                          alt="User Image" />
                      </div>
                    </template>
                    <template v-else-if="column.key === 'Status'">
                      <div class="status-toggle">
                        <input :id="record.id" class="check" type="checkbox" checked="" />
                        <label :for="record.for" class="checktoggle checkbox-bg">checkbox</label>
                      </div>
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="d-flex align-items-center">
                        <a class="btn-action-icon active me-2" href="javascript:void(0);" data-bs-toggle="tooltip"
                          title="" data-bs-placement="left">
                          <a-tooltip title="Remove default" placement="left">
                            <i class="feather feather-star"></i>
                          </a-tooltip>
                        </a>
                        <a class="btn-action-icon me-2" href="javascript:void(0);" data-bs-toggle="modal"
                          data-bs-target="#edit_modal"><i class="feather feather-edit"></i></a>
                        <a class="btn-action-icon" href="javascript:void(0);" data-bs-toggle="modal"
                          data-bs-target="#warning_modal"><i class="feather feather-trash-2"></i></a>
                      </div>
                    </template>
                  </template>
                </a-table>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Table -->
    </div>
  </div>
  <signatureedit></signatureedit>
</template>
<script>
import { Tooltip, Button } from "ant-design-vue";

export default {
  components: {
    "a-tooltip": Tooltip,
    "a-button": Button,
  },
  setup() {
    return {
      columns,
      data,
    };
  },
};
const columns = [
  {
    title: "#",
    dataIndex: "NUM",
    sorter: {
      compare: (a, b) => {
        a = a.NUM.toLowerCase();
        b = b.NUM.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Signature Name",
    dataIndex: "SignatureName",
    sorter: {
      compare: (a, b) => {
        a = a.SignatureName.toLowerCase();
        b = b.SignatureName.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Signature",
    dataIndex: "Signature",
    key: "Name",
    sorter: {
      compare: (a, b) => {
        a = a.Signature.toLowerCase();
        b = b.Signature.toLowerCase();
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
    NUM: "1",
    id: "rating_1",
    for: "rating_1",
    SignatureName: "Allen",
    Signature: "user-signature.png",
    Status: "checkbox",
    Action: "",
  },
  {
    NUM: "2",
    SignatureName: "Raymond",
    id: "rating_2",
    for: "rating_2",
    Signature: "user-signature.png",
    Status: "checkbox",
    Action: "",
  },
  {
    NUM: "3",
    SignatureName: "Ralph",
    id: "rating_3",
    for: "rating_3",
    Signature: "user-signature.png",
    Status: "checkbox",
    Action: "",
  },
  {
    NUM: "4",
    SignatureName: "Ruth",
    id: "rating_4",
    for: "rating_4",
    Signature: "user-signature.png",
    Status: "checkbox",
    Action: "",
  },
  {
    NUM: "5",
    SignatureName: "Steven",
    id: "rating_5",
    for: "rating_5",
    Signature: "user-signature.png",
    Status: "checkbox",
    Action: "",
  },
  {
    NUM: "6",
    SignatureName: "Earnes",
    id: "rating_6",
    for: "rating_6",
    Signature: "user-signature.png",
    Status: "checkbox",
    Action: "",
  },
];
</script>
