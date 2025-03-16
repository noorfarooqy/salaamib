<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <taxpurchase-header :title="title" />
      <!-- /Page Header -->

      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <div class="companies-table">
                  <a-table class="table table-center table-hover datatable" :columns="columns" :data-source="data">
                    <template #bodyCell="{ column, record }">
                      <template v-if="column.key === 'id'">
                        <div>{{ record.id }}</div>
                      </template>
                    </template>
                  </a-table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Search Filter -->
      <div id="filter_inputs" class="card filter-card">
        <div class="card-body pb-0">
          <div class="row">
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Name</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Email</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Phone</label>
                <input type="text" class="form-control" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Search Filter -->
    </div>
  </div>
  <taxpurchasemodel></taxpurchasemodel>
</template>
<script>
const columns = [
  {
    title: "#",
    dataIndex: "id",
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.id.toLowerCase();
        b = b.id.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },

  {
    title: "Supplier",
    dataIndex: "Supplier",
    sorter: {
      compare: (a, b) => {
        a = a.Supplier.toLowerCase();
        b = b.Supplier.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Date",
    dataIndex: "Date",
    sorter: {
      compare: (a, b) => {
        a = a.Date.toLowerCase();
        b = b.Date.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Ref No",
    dataIndex: "RefNo",
    sorter: {
      compare: (a, b) => {
        a = a.RefNo.toLowerCase();
        b = b.RefNo.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Total Amount",
    dataIndex: "TotalAmount",
    sorter: {
      compare: (a, b) => {
        a = a.TotalAmount.toLowerCase();
        b = b.TotalAmount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Payment Method",
    dataIndex: "PaymentMethod",
    sorter: {
      compare: (a, b) => {
        a = a.PaymentMethod.toLowerCase();
        b = b.PaymentMethod.toLowerCase();
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
    title: "Tax Amount",
    dataIndex: "TaxAmount",
    sorter: {
      compare: (a, b) => {
        a = a.TaxAmount.toLowerCase();
        b = b.TaxAmount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  }
];
const data = [
  {
    id: "1",
    Supplier: "Michael",
    Date: "01 Aug 2023",
    RefNo: "#312345",
    TotalAmount: "$3000.00",
    PaymentMethod: "Cash",
    Discount: "12",
    TaxAmount: "$375",
  },
  {
    id: "2",
    Supplier: "Richard",
    Date: "12 Aug 2023",
    RefNo: "#236348",
    TotalAmount: "$2000.00",
    PaymentMethod: "Cash",
    Discount: "8",
    TaxAmount: "$247",
  },
  {
    id: "3",
    Supplier: "Joseph",
    Date: "16 Sep 2023",
    RefNo: "#395374",
    TotalAmount: "$17200.00",
    PaymentMethod: "Cash",
    Discount: "10",
    TaxAmount: "$172",
  },
  {
    id: "4",
    Supplier: "David",
    Date: "24 Sep 2023",
    RefNo: "#312345",
    TotalAmount: "$32000.00",
    PaymentMethod: "Cash",
    Discount: "14",
    TaxAmount: "$590",
  },
  {
    id: "5",
    Supplier: "Benjamin",
    Date: "19 Oct 2023",
    RefNo: "#893246",
    TotalAmount: "$24000.00",
    PaymentMethod: "Cash",
    Discount: "12",
    TaxAmount: "$375",
  },
  {
    id: "6",
    Supplier: "Steven",
    Date: "20 Oct 2023",
    RefNo: "#457289",
    TotalAmount: "$12000.00",
    PaymentMethod: "Cash",
    Discount: "5",
    TaxAmount: "$440",
  },
];
export default {
  data() {
    return {
      title: "Tax Report",
      data,
      columns,
    };
  },
};
</script>
