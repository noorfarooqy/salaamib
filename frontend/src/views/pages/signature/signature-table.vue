<template>
  <a-table class="stripped table-hover" :columns="columns" :data-source="data">
    <template #bodyCell="{ column }">
      <template v-if="column.key === 'id'">
        <input type="number" class="form-control" value="0" />
      </template>
      <template v-else-if="column.key === 'rate'">
        <input type="number" class="form-control" placeholder="120" />
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
    Unit: "Pcs",
    Rate: "$120.00",
    Discount: "0",
    Tax: "0",
    Amount: "$120.00",
  },
];
export default {
  data() {
    return {
      columns,
      data,
    };
  },
};
</script>
