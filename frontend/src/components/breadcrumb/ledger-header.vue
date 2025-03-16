<template>
  <div class="page-header">
    <div class="content-page-header">
      <h5>{{ title }}</h5>
      <div class="list-btn">
        <ul class="filter-list">
          <li>
            <a
              class="btn btn-filters w-auto popup-toggle"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="Filter"
              ><span class="me-2"
                ><img src="@/assets/img/icons/filter-icon.svg" alt="filter" /></span
              >Filter
            </a>
          </li>
          <li>
            <a
              class="btn-filters"
              href="javascript:void(0);"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="Grid-View"
              ><span><i class="feather feather-grid"></i></span>
            </a>
          </li>
          <li>
            <a
              class="active btn-filters"
              href="javascript:void(0);"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="List-View"
              ><span><i class="feather feather-list"></i></span>
            </a>
          </li>
          <li>
            <a
              class="btn btn-primary"
              href="#"
              data-bs-toggle="modal"
              data-bs-target="#add_ledger"
              ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i>{{ text }}</a
            >
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    title: {
      type: String,
      default: "",
    },
    text: {
      type: String,
      default: "",
    },
  },
};
</script>
