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
          <li class="daterangepicker-wrap cal-icon cal-icon-info">
            <input
              type="text"
              class="btn-filters"
              name="datetimes"
              ref="dateRangeInput"
              placeholder="From Date - To Date"
            />
            <i class="feather feather-calendar calendar-icon"></i>
          </li>
          <li>
            <div
              class="dropdown dropdown-action"
              data-bs-toggle="tooltip"
              data-bs-placement="top"
              title="Download"
            >
              <a
                href="javascript:;"
                class="btn-filters"
                data-bs-toggle="dropdown"
                aria-expanded="false"
                ><span><i class="feather feather-download"></i></span
              ></a>
              <div class="dropdown-menu dropdown-menu-end">
                <ul class="d-block">
                  <li>
                    <a
                      class="d-flex align-items-center download-item"
                      href="javascript:void(0);"
                      download
                      ><i class="far fa-file-pdf me-2"></i>PDF</a
                    >
                  </li>
                  <li>
                    <a
                      class="d-flex align-items-center download-item"
                      href="javascript:void(0);"
                      download
                      ><i class="far fa-file-text me-2"></i>CVS</a
                    >
                  </li>
                </ul>
              </div>
            </div>
          </li>
          <li>
            <a
              class="btn-filters"
              href="javascript:void(0);"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="Print"
              ><span><i class="feather feather-printer"></i></span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
import "daterangepicker/daterangepicker.css";
import "daterangepicker/daterangepicker.js";
// import "moment/min/moment.min.js";
import { ref } from "vue";
import { onMounted } from "vue";
import moment from "moment";
import DateRangePicker from "daterangepicker";
export default {
  props: {
    title: {
      type: String,
      default: "",
    },
  },
  data() {
    return {};
  },
  setup() {
    const dateRangeInput = ref(null);
    onMounted(() => {
      if (dateRangeInput.value) {
        const start = moment().subtract(6, "days");
        const end = moment();

        function booking_range(start, end) {
          start.format("M/D/YYYY") + " - " + end.format("M/D/YYYY");
        }

        new DateRangePicker(
          dateRangeInput.value,
          {
            startDate: start,
            endDate: end,
          },
          booking_range
        );

        booking_range(start, end);
      }
    });
    return {
      dateRangeInput,
    };
  },
};
</script>
